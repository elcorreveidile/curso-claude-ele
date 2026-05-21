"""Module routes: course content and progress."""
from fastapi import APIRouter, HTTPException

from core import supabase
from models import ModuleOut
from seed_content.modules_data import MODULES

router = APIRouter(prefix="/modules", tags=["modules"])


@router.get("")
async def get_modules(current_user: dict = None) -> list[ModuleOut]:
    """Get all modules with user progress."""
    from core import current_user as get_user
    from fastapi import Depends

    user = await get_user()
    enrollment_id = user["id"]

    # Get user's module progress
    progress_result = supabase.table("module_progress").select("*").eq("enrollment_id", enrollment_id).execute()
    progress_map = {p["module_id"]: p for p in progress_result.data}

    # Build modules with status
    modules_with_status = []
    for module in MODULES:
        progress = progress_map.get(module["id"])
        status = "locked"

        if progress:
            status = progress["status"]
        elif module["unlock_rule"] == "always_open":
            status = "available"
        elif module["unlock_rule"] == "on_enrollment":
            status = "available"

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
async def get_module(module_id: str, current_user: dict = None) -> dict:
    """Get module details with content."""
    from core import current_user as get_user
    from fastapi import Depends

    user = await get_user()

    # Find module
    module = next((m for m in MODULES if m["id"] == module_id), None)
    if not module:
        raise HTTPException(404, "Módulo no encontrado")

    # Check if user has access (not locked)
    enrollment_id = user["id"]
    progress_result = supabase.table("module_progress").select("*").eq("enrollment_id", enrollment_id).eq("module_id", module_id).execute()

    if not progress_result.data:
        raise HTTPException(403, "No tienes acceso a este módulo")

    progress = progress_result.data[0]
    if progress["status"] == "locked":
        raise HTTPException(403, "Este módulo está bloqueado")

    return {
        **module,
        "status": progress["status"],
        "unlocked_at": progress.get("unlocked_at"),
        "completed_at": progress.get("completed_at"),
    }


@router.get("/progress")
async def get_progress(current_user: dict = None) -> dict:
    """Get user's overall progress."""
    from core import current_user as get_user
    from fastapi import Depends

    user = await get_user()
    enrollment_id = user["id"]

    # Get all module progress
    progress_result = supabase.table("module_progress").select("*").eq("enrollment_id", enrollment_id).execute()

    total = len(progress_result.data)
    completed = sum(1 for p in progress_result.data if p["status"] == "completed")

    return {
        "total": total,
        "completed": completed,
        "percent": round((completed / total * 100) if total > 0 else 0),
    }


@router.post("/{module_id}/complete")
async def complete_module(module_id: str, current_user: dict = None) -> dict:
    """Mark module as completed."""
    from core import current_user as get_user, now_utc
    from fastapi import Depends

    user = await get_user()
    enrollment_id = user["id"]

    # Update module progress
    result = supabase.table("module_progress").update({
        "status": "completed",
        "completed_at": now_utc().isoformat(),
    }).eq("enrollment_id", enrollment_id).eq("module_id", module_id).execute()

    if not result.data:
        raise HTTPException(404, "Progreso de módulo no encontrado")

    return {"message": "Módulo marcado como completado"}
