"""Admin routes: stats, participants, sessions, certificates."""
from fastapi import APIRouter, Depends, HTTPException

from core import ADMIN_EMAIL, new_id, now_utc, send_email, supabase, wrap_email
from core import current_admin
from models import AdminStatsOut, CertificateOut, ParticipantOut, SessionOut
from seed_content.modules_data import MODULES

router = APIRouter(prefix="/admin", tags=["admin"])


@router.get("/stats")
async def get_admin_stats(admin: dict = Depends(current_admin)) -> AdminStatsOut:
    enrollments_result = supabase.table("enrollments").select("*", count="exact").execute()
    total_enrollments = enrollments_result.count or 0

    active_result = supabase.table("enrollments").select("*", count="exact").eq("status", "active").execute()
    active_students = active_result.count or 0

    completed_result = supabase.table("module_progress").select("*", count="exact").eq("status", "completed").execute()
    completed_modules = completed_result.count or 0

    pending_result = supabase.table("task_submissions").select("*", count="exact").is_("feedback", "null").execute()
    pending_feedback = pending_result.count or 0

    return AdminStatsOut(
        total_enrollments=total_enrollments,
        active_students=active_students,
        completed_modules=completed_modules,
        pending_feedback=pending_feedback,
    )


@router.get("/participants")
async def get_participants(admin: dict = Depends(current_admin)) -> list[ParticipantOut]:
    result = supabase.table("enrollments").select("*").order("enrolled_at", desc=True).execute()

    participants = []
    for enrollment in result.data:
        progress_result = (
            supabase.table("module_progress")
            .select("*", count="exact")
            .eq("enrollment_id", enrollment["id"])
            .eq("status", "completed")
            .execute()
        )
        completed_count = progress_result.count or 0
        participants.append(
            ParticipantOut(
                id=enrollment["id"],
                email=enrollment["email"],
                name=enrollment.get("name"),
                enrolled_at=enrollment["enrolled_at"],
                status=enrollment["status"],
                completed_modules=completed_count,
                total_modules=len(MODULES),
            )
        )
    return participants


@router.get("/sessions")
async def get_sessions(admin: dict = Depends(current_admin)) -> list[SessionOut]:
    result = supabase.table("live_sessions").select("*").order("session_num").execute()
    return [
        SessionOut(
            id=s["id"],
            session_num=s["session_num"],
            title=s["title"],
            scheduled_at=s.get("scheduled_at"),
            zoom_link=s.get("zoom_link"),
            recording_url=s.get("recording_url"),
            status=s["status"],
        )
        for s in result.data
    ]


@router.post("/sessions")
async def create_session(
    session_num: int,
    title: str,
    scheduled_at: str = None,
    admin: dict = Depends(current_admin),
) -> dict:
    existing = supabase.table("live_sessions").select("*").eq("session_num", session_num).execute()
    if existing.data:
        raise HTTPException(400, f"La sesión {session_num} ya existe")

    result = supabase.table("live_sessions").insert({
        "session_num": session_num,
        "title": title,
        "scheduled_at": scheduled_at,
        "status": "scheduled",
    }).execute()

    if not result.data:
        raise HTTPException(500, "Error al crear sesión")
    return {"message": "Sesión creada correctamente", "session": result.data[0]}


@router.patch("/sessions/{session_id}")
async def update_session(
    session_id: str,
    title: str = None,
    scheduled_at: str = None,
    zoom_link: str = None,
    recording_url: str = None,
    admin: dict = Depends(current_admin),
) -> dict:
    updates = {k: v for k, v in {
        "title": title,
        "scheduled_at": scheduled_at,
        "zoom_link": zoom_link,
        "recording_url": recording_url,
    }.items() if v is not None}

    if not updates:
        raise HTTPException(400, "No hay campos para actualizar")

    result = supabase.table("live_sessions").update(updates).eq("id", session_id).execute()
    if not result.data:
        raise HTTPException(404, "Sesión no encontrada")
    return {"message": "Sesión actualizada", "session": result.data[0]}


@router.post("/sessions/{session_id}/complete")
async def complete_session(session_id: str, admin: dict = Depends(current_admin)) -> dict:
    """Mark session as completed and unlock the corresponding modules."""
    session_result = supabase.table("live_sessions").select("*").eq("id", session_id).execute()
    if not session_result.data:
        raise HTTPException(404, "Sesión no encontrada")

    session = session_result.data[0]
    session_num = session["session_num"]

    supabase.table("live_sessions").update({"status": "completed"}).eq("id", session_id).execute()

    modules_to_unlock = {
        1: ["modulo-3"],
        2: ["modulo-4", "modulo-5"],
        3: ["modulo-6"],
    }.get(session_num, [])

    if not modules_to_unlock:
        return {"message": f"Sesión {session_num} completada. Sin módulos adicionales para desbloquear."}

    enrollments = supabase.table("enrollments").select("id, email, name").eq("status", "active").execute()
    now_iso = now_utc().isoformat()

    for enrollment in enrollments.data:
        for module_id in modules_to_unlock:
            supabase.table("module_progress").update({
                "status": "available",
                "unlocked_at": now_iso,
            }).eq("enrollment_id", enrollment["id"]).eq("module_id", module_id).execute()

    # Email notifications
    for enrollment in enrollments.data:
        modules_info = []
        for module_id in modules_to_unlock:
            module = next((m for m in MODULES if m["id"] == module_id), None)
            if module:
                modules_info.append(f"Módulo {module['num']}: {module['title']}")

        html = wrap_email(f"""
          <h2 style="font-family:sans-serif;font-size:1.5rem;font-weight:800;color:#0F4C81;margin-bottom:1rem;">
            ¡Nuevo módulo disponible!
          </h2>
          <p style="font-size:1rem;color:#2E4260;line-height:1.7;margin-bottom:1rem;">
            Hola <strong>{enrollment.get('name', 'Estudiante')}</strong>, ya puedes acceder a:
          </p>
          <ul style="font-size:1rem;color:#2E4260;line-height:1.7;margin:2rem 0;padding-left:1.5rem;">
            {"".join(f'<li style="margin-bottom:0.5rem;"><strong>{info}</strong></li>' for info in modules_info)}
          </ul>
        """)
        await send_email(
            to_email=enrollment["email"],
            subject=f"Ya puedes acceder al nuevo módulo — Sesión {session_num} completada",
            html=html,
        )

    return {"message": f"Sesión completada. Módulos desbloqueados: {', '.join(modules_to_unlock)}"}


@router.post("/certificates/generate")
async def generate_certificate(enrollment_id: str, admin: dict = Depends(current_admin)) -> dict:
    enrollment_result = supabase.table("enrollments").select("*").eq("id", enrollment_id).execute()
    if not enrollment_result.data:
        raise HTTPException(404, "Inscripción no encontrada")

    enrollment = enrollment_result.data[0]

    existing_cert = supabase.table("certificates").select("*").eq("enrollment_id", enrollment_id).execute()
    if existing_cert.data:
        return {"message": "Certificado ya existe", "certificate": existing_cert.data[0]}

    verification_code = new_id()[:12]
    cert_result = supabase.table("certificates").insert({
        "enrollment_id": enrollment_id,
        "name": enrollment.get("name", enrollment["email"]),
        "verification_code": verification_code,
    }).execute()

    if not cert_result.data:
        raise HTTPException(500, "Error al generar certificado")

    supabase.table("enrollments").update({
        "status": "completed",
        "completed_at": now_utc().isoformat(),
    }).eq("id", enrollment_id).execute()

    html = wrap_email(f"""
      <div style="text-align:center;margin-bottom:2rem;">
        <span style="font-family:Georgia,serif;font-size:3rem;color:#F5A623;letter-spacing:-3px;">[|]</span>
      </div>
      <h1 style="font-family:sans-serif;font-size:1.8rem;font-weight:800;color:#0F4C81;margin-bottom:1rem;">
        ¡Felicidades!
      </h1>
      <p style="font-size:1.1rem;color:#2E4260;line-height:1.7;margin-bottom:1.5rem;">
        Hola <strong>{enrollment.get('name', 'Estudiante')}</strong>, has completado el curso
        <strong>Claude para la enseñanza: domina la herramienta</strong>.
      </p>
      <div style="background:#EDF4FB;border:1px solid #0F4C81;border-radius:12px;padding:2rem;margin:2rem 0;text-align:center;">
        <p style="font-size:0.9rem;color:#6B82A0;margin-bottom:0.5rem;">Código de verificación:</p>
        <p style="font-size:1.5rem;font-family:monospace;font-weight:700;color:#0F4C81;">{verification_code}</p>
      </div>
      <p style="font-size:0.9rem;color:#6B82A0;line-height:1.6;">
        Descarga tu certificado desde tu área de estudiante.
      </p>
    """)
    await send_email(
        to_email=enrollment["email"],
        subject="Tu certificado ya está listo",
        html=html,
    )

    return {"message": "Certificado generado correctamente", "certificate": cert_result.data[0]}


@router.get("/certificates")
async def list_certificates(admin: dict = Depends(current_admin)) -> list[dict]:
    result = supabase.table("certificates").select("*, enrollments(email, name)").execute()
    return result.data
