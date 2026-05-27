"""Module routes: course content and user progress."""
from fastapi import APIRouter, Depends, HTTPException

from core import current_user, now_utc, supabase
from models import ModuleOut
from seed_content.modules_data import MODULES

router = APIRouter(prefix="/modules", tags=["modules"])


@router.get("/progress")
async def get_progress(user: dict = Depends(current_user)) -> dict:
    """Overall progress summary for the authenticated user."""
    enrollment_id = user["id"]
    progress_result = (
        supabase.table("module_progress")
        .select("*")
        .eq("enrollment_id", enrollment_id)
        .execute()
    )
    total = len(progress_result.data)
    completed = sum(1 for p in progress_result.data if p["status"] == "completed")
    return {
        "total": total,
        "completed": completed,
        "percent": round((completed / total * 100) if total > 0 else 0),
    }


@router.get("")
async def get_modules(user: dict = Depends(current_user)) -> list[ModuleOut]:
    """All modules with the user's current status."""
    enrollment_id = user["id"]
    progress_result = (
        supabase.table("module_progress")
        .select("*")
        .eq("enrollment_id", enrollment_id)
        .execute()
    )
    progress_map = {p["module_id"]: p for p in progress_result.data}

    modules_with_status = []
    for module in MODULES:
        progress = progress_map.get(module["id"])
        if progress:
            status = progress["status"]
        elif module["unlock_rule"] in ("always_open", "on_enrollment"):
            status = "available"
        else:
            status = "locked"

        modules_with_status.append(
            ModuleOut(
                id=module["id"],
                num=module["num"],
                title=module["title"],
                subtitle=module["subtitle"],
                hours=module["hours"],
                optional=module.get("optional", False),
                status=status,
                videos=module.get("videos", []),
                readings=module.get("readings", []),
                activities=module.get("activities", []),
            )
        )
    return modules_with_status


@router.get("/{module_id}")
async def get_module(module_id: str, user: dict = Depends(current_user)) -> dict:
    """Single module with content (requires access)."""
    module = next((m for m in MODULES if m["id"] == module_id), None)
    if not module:
        raise HTTPException(404, "Módulo no encontrado")

    enrollment_id = user["id"]
    progress_result = (
        supabase.table("module_progress")
        .select("*")
        .eq("enrollment_id", enrollment_id)
        .eq("module_id", module_id)
        .execute()
    )

    if not progress_result.data:
        # Module 0 is always accessible even before progress rows exist
        if module.get("unlock_rule") == "always_open":
            status = "available"
        else:
            raise HTTPException(403, "No tienes acceso a este módulo")
    else:
        progress = progress_result.data[0]
        status = progress["status"]
        if status == "locked":
            raise HTTPException(403, "Este módulo está bloqueado")

    return {
        **module,
        "status": status,
    }


@router.post("/{module_id}/complete")
async def complete_module(module_id: str, user: dict = Depends(current_user)) -> dict:
    """Mark a module as completed."""
    enrollment_id = user["id"]
    result = (
        supabase.table("module_progress")
        .update({"status": "completed", "completed_at": now_utc().isoformat()})
        .eq("enrollment_id", enrollment_id)
        .eq("module_id", module_id)
        .execute()
    )
    if not result.data:
        raise HTTPException(404, "Progreso de módulo no encontrado")
    return {"message": "Módulo marcado como completado"}
