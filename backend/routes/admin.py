"""Admin routes: stats, participants, sessions, certificates."""
import uuid
from fastapi import APIRouter, HTTPException

from core import ADMIN_EMAIL, new_id, now_utc, send_email, supabase, wrap_email
from models import AdminStatsOut, CertificateOut, ParticipantOut, SessionOut
from seed_content.modules_data import MODULES

router = APIRouter(prefix="/admin", tags=["admin"])


@router.get("/stats")
async def get_admin_stats(current_user: dict = None) -> AdminStatsOut:
    """Get admin dashboard stats."""
    from core import current_admin
    from fastapi import Depends

    await current_admin()

    # Total enrollments
    enrollments_result = supabase.table("enrollments").select("*", count="exact").execute()
    total_enrollments = enrollments_result.count if enrollments_result.count else 0

    # Active students
    active_result = supabase.table("enrollments").select("*", count="exact").eq("status", "active").execute()
    active_students = active_result.count if active_result.count else 0

    # Completed modules
    completed_result = supabase.table("module_progress").select("*", count="exact").eq("status", "completed").execute()
    completed_modules = completed_result.count if completed_result.count else 0

    # Pending feedback (submissions without feedback)
    pending_result = supabase.table("task_submissions").select("*", count="exact").is_("feedback", "null").execute()
    pending_feedback = pending_result.count if pending_result.count else 0

    return AdminStatsOut(
        total_enrollments=total_enrollments,
        active_students=active_students,
        completed_modules=completed_modules,
        pending_feedback=pending_feedback,
    )


@router.get("/participants")
async def get_participants(current_user: dict = None) -> list[ParticipantOut]:
    """Get all participants."""
    from core import current_admin
    from fastapi import Depends

    await current_admin()

    # Get all enrollments
    result = supabase.table("enrollments").select("*").order("enrolled_at", desc=True).execute()

    participants = []
    for enrollment in result.data:
        # Count completed modules
        progress_result = supabase.table("module_progress").select("*", count="exact").eq("enrollment_id", enrollment["id"]).eq("status", "completed").execute()
        completed_count = progress_result.count if progress_result.count else 0

        participants.append(
            ParticipantOut(
                id=enrollment["id"],
                email=enrollment["email"],
                name=enrollment.get("name"),
                enrolled_at=enrollment["enrolled_at"],
                status=enrollment["status"],
                completed_modules=completed_count,
                total_modules=len(MODULES) - 1,  # Exclude optional module from total
            )
        )

    return participants


@router.get("/sessions")
async def get_sessions(current_user: dict = None) -> list[SessionOut]:
    """Get all live sessions."""
    from core import current_admin
    from fastapi import Depends

    await current_admin()

    result = supabase.table("live_sessions").select("*").order("session_num").execute()

    return [
        SessionOut(
            id=session["id"],
            session_num=session["session_num"],
            title=session["title"],
            scheduled_at=session.get("scheduled_at"),
            zoom_link=session.get("zoom_link"),
            recording_url=session.get("recording_url"),
            status=session["status"],
        )
        for session in result.data
    ]


@router.post("/sessions")
async def create_session(
    session_num: int,
    title: str,
    scheduled_at: str = None,
    current_user: dict = None,
) -> dict:
    """Create new live session."""
    from core import current_admin
    from fastapi import Depends

    await current_admin()

    # Check if session_num already exists
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


@router.post("/sessions/{session_id}/complete")
async def complete_session(session_id: str, current_user: dict = None) -> dict:
    """Mark session as completed and unlock next modules."""
    from core import current_admin, now_utc
    from fastapi import Depends

    await current_admin()

    # Get session
    session_result = supabase.table("live_sessions").select("*").eq("id", session_id).execute()
    if not session_result.data:
        raise HTTPException(404, "Sesión no encontrada")

    session = session_result.data[0]
    session_num = session["session_num"]

    # Mark session as completed
    supabase.table("live_sessions").update({
        "status": "completed",
    }).eq("id", session_id).execute()

    # Unlock modules based on session completed
    modules_to_unlock = []
    if session_num == 1:
        modules_to_unlock = ["modulo-3"]
    elif session_num == 2:
        modules_to_unlock = ["modulo-4", "modulo-5"]
    elif session_num == 3:
        modules_to_unlock = ["modulo-6"]

    # Get all active enrollments
    enrollments = supabase.table("enrollments").select("id").eq("status", "active").execute()

    for enrollment in enrollments.data:
        for module_id in modules_to_unlock:
            # Update module progress to available
            supabase.table("module_progress").update({
                "status": "available",
                "unlocked_at": now_utc().isoformat(),
            }).eq("enrollment_id", enrollment["id"]).eq("module_id", module_id).execute()

    # Send email notifications about unlocked modules
    if modules_to_unlock:
        for enrollment in enrollments.data:
            enrollment_data = supabase.table("enrollments").select("*").eq("id", enrollment["id"]).execute()
            if enrollment_data.data:
                student_email = enrollment_data.data[0]["email"]
                student_name = enrollment_data.data[0].get("name", "Estudiante")

                modules_info = []
                for module_id in modules_to_unlock:
                    module = next((m for m in MODULES if m["id"] == module_id), None)
                    if module:
                        modules_info.append(f"Módulo {module['num']}: {module['title']}")

                html = wrap_email(f"""
                  <h2 style="font-family:var(--font-display);font-size:1.5rem;font-weight:800;color:#0F4C81;margin-bottom:1rem;">
                    ¡Nuevo módulo disponible!
                  </h2>
                  <p style="font-size:1rem;color:#2E4260;line-height:1.7;margin-bottom:1rem;">
                    Hola <strong>{student_name}</strong>, ya puedes acceder a nuevos contenidos del curso:
                  </p>
                  <ul style="font-size:1rem;color:#2E4260;line-height:1.7;margin:2rem 0;padding-left:1.5rem;">
                    {"".join(f'<li style="margin-bottom:0.5rem;"><strong>{info}</strong></li>' for info in modules_info)}
                  </ul>
                  <p style="font-size:0.9rem;color:#6B82A0;line-height:1.6;">
                    Accede a tu área para continuar con el curso.
                  </p>
                """)

                await send_email(
                    to_email=student_email,
                    subject=f"Ya puedes acceder al Módulo {session_num + 1}",
                    html=html,
                )

    return {"message": f"Sesión completada. Módulos desbloqueados: {', '.join(modules_to_unlock)}"}


@router.post("/certificates/generate")
async def generate_certificate(enrollment_id: str, current_user: dict = None) -> dict:
    """Generate certificate for enrollment."""
    from core import current_admin, now_utc
    from fastapi import Depends

    await current_admin()

    # Get enrollment
    enrollment_result = supabase.table("enrollments").select("*").eq("id", enrollment_id).execute()
    if not enrollment_result.data:
        raise HTTPException(404, "Inscripción no encontrada")

    enrollment = enrollment_result.data[0]

    # Check if certificate already exists
    existing_cert = supabase.table("certificates").select("*").eq("enrollment_id", enrollment_id).execute()
    if existing_cert.data:
        return {"message": "Certificado ya existe", "certificate": existing_cert.data[0]}

    # Generate verification code
    verification_code = new_id()[:12]

    # Create certificate
    cert_result = supabase.table("certificates").insert({
        "enrollment_id": enrollment_id,
        "name": enrollment.get("name", enrollment["email"]),
        "verification_code": verification_code,
    }).execute()

    if not cert_result.data:
        raise HTTPException(500, "Error al generar certificado")

    # Update enrollment status
    supabase.table("enrollments").update({
        "status": "completed",
        "completed_at": now_utc().isoformat(),
    }).eq("id", enrollment_id).execute()

    # Send certificate email
    html = wrap_email(f"""
      <div style="text-align:center;margin-bottom:2rem;">
        <span style="font-family:Georgia,serif;font-size:3rem;color:#F5A623;letter-spacing:-3px;">
          [|]
        </span>
      </div>
      <h1 style="font-family:var(--font-display);font-size:1.8rem;font-weight:800;color:#0F4C81;margin-bottom:1rem;">
        ¡Felicidades!
      </h1>
      <p style="font-size:1.1rem;color:#2E4260;line-height:1.7;margin-bottom:1.5rem;">
        Hola <strong>{enrollment.get('name', 'Estudiante')}</strong>, has completado satisfactoriamente el curso
        <strong>Claude para la enseñanza: domina la herramienta</strong>.
      </p>
      <div style="background:#EDF4FB;border:1px solid #0F4C81;border-radius:12px;padding:2rem;margin:2rem 0;text-align:center;">
        <p style="font-size:1.2rem;color:#0F4C81;font-weight:700;margin-bottom:1rem;">
          Tu certificado de aprovechamiento está listo
        </p>
        <p style="font-size:0.9rem;color:#6B82A0;margin-bottom:0.5rem;">
          Código de verificación:
        </p>
        <p style="font-size:1.5rem;font-family:monospace;font-weight:700;color:#0F4C81;">
          {verification_code}
        </p>
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


@router.get("/certificates/my")
async def get_my_certificate(current_user: dict = None) -> CertificateOut:
    """Get current user's certificate."""
    from core import current_user
    from fastapi import Depends

    user = await current_user()

    result = supabase.table("certificates").select("*").eq("enrollment_id", user["id"]).execute()

    if not result.data:
        raise HTTPException(404, "Certificado no disponible")

    cert = result.data[0]
    return CertificateOut(
        name=cert["name"],
        verification_code=cert["verification_code"],
        issued_at=cert["issued_at"],
    )
