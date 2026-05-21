"""Task routes: activities, submissions, and feedback."""
from fastapi import APIRouter, HTTPException

from core import now_utc, send_email, supabase, wrap_email
from models import FeedbackIn, SubmissionIn, SubmissionOut, TaskOut
from seed_content.modules_data import MODULES

router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.get("")
async def get_tasks(current_user: dict = None) -> list[TaskOut]:
    """Get all tasks for user."""
    from core import current_user as get_user
    from fastapi import Depends

    user = await get_user()
    enrollment_id = user["id"]

    # Get accessible modules
    progress_result = supabase.table("module_progress").select("*").eq("enrollment_id", enrollment_id).in_("status", ["available", "in_progress", "completed"]).execute()
    accessible_module_ids = [p["module_id"] for p in progress_result.data]

    # Get all activities from accessible modules
    tasks = []
    for module in MODULES:
        if module["id"] in accessible_module_ids:
            for activity in module.get("activities", []):
                tasks.append(
                    TaskOut(
                        id=activity["id"],
                        module_id=module["id"],
                        title=activity["title"],
                        description=activity.get("description", ""),
                        duration=activity.get("duration", ""),
                        requires_submission=activity.get("requires_submission", False),
                    )
                )

    return tasks


@router.get("/{task_id}")
async def get_task(task_id: str, current_user: dict = None) -> dict:
    """Get task details."""
    from core import current_user as get_user
    from fastapi import Depends

    user = await get_user()

    # Find task in modules
    for module in MODULES:
        for activity in module.get("activities", []):
            if activity["id"] == task_id:
                return {
                    "id": activity["id"],
                    "module_id": module["id"],
                    **activity,
                }

    raise HTTPException(404, "Actividad no encontrada")


@router.get("/{task_id}/submission")
async def get_submission(task_id: str, current_user: dict = None) -> SubmissionOut:
    """Get task submission."""
    from core import current_user as get_user
    from fastapi import Depends

    user = await get_user()
    enrollment_id = user["id"]

    result = supabase.table("task_submissions").select("*").eq("enrollment_id", enrollment_id).eq("activity_id", task_id).execute()

    if not result.data:
        raise HTTPException(404, "No hay entrega para esta actividad")

    submission = result.data[0]
    return SubmissionOut(
        id=submission["id"],
        content=submission["content"],
        submitted_at=submission["submitted_at"],
        feedback=submission.get("feedback"),
        feedback_at=submission.get("feedback_at"),
    )


@router.post("/{task_id}/submit")
async def submit_task(task_id: str, submission: SubmissionIn, current_user: dict = None) -> dict:
    """Submit task."""
    from core import current_user as get_user, now_utc
    from fastapi import Depends

    user = await get_user()
    enrollment_id = user["id"]

    # Find task's module_id
    module_id = None
    for module in MODULES:
        for activity in module.get("activities", []):
            if activity["id"] == task_id:
                module_id = module["id"]
                break
        if module_id:
            break

    if not module_id:
        raise HTTPException(404, "Actividad no encontrada")

    # Create submission
    result = supabase.table("task_submissions").insert({
        "enrollment_id": enrollment_id,
        "activity_id": task_id,
        "module_id": module_id,
        "content": submission.content,
        "submitted_at": now_utc().isoformat(),
    }).execute()

    if not result.data:
        raise HTTPException(500, "Error al crear entrega")

    return {"message": "Actividad entregada correctamente"}


@router.post("/{task_id}/feedback")
async def give_feedback(task_id: str, feedback: FeedbackIn, current_user: dict = None) -> dict:
    """Give feedback on task submission (admin only)."""
    from core import current_admin, now_utc
    from fastapi import Depends

    admin = await current_admin()

    # Get submission
    result = supabase.table("task_submissions").select("*").eq("activity_id", task_id).execute()

    if not result.data:
        raise HTTPException(404, "Entrega no encontrada")

    submission = result.data[0]

    # Update submission with feedback
    update_result = supabase.table("task_submissions").update({
        "feedback": feedback.feedback,
        "feedback_at": now_utc().isoformat(),
    }).eq("id", submission["id"]).execute()

    # Get enrollment to send email
    enrollment = supabase.table("enrollments").select("*").eq("id", submission["enrollment_id"]).execute()
    if enrollment.data:
        student_email = enrollment.data[0]["email"]
        student_name = enrollment.data[0].get("name", "Estudiante")

        # Find task title
        task_title = ""
        for module in MODULES:
            for activity in module.get("activities", []):
                if activity["id"] == task_id:
                    task_title = activity["title"]
                    break
            if task_title:
                break

        # Send feedback email
        html = wrap_email(f"""
          <h2 style="font-family:var(--font-display);font-size:1.5rem;font-weight:800;color:#0F4C81;margin-bottom:1rem;">
            Tienes feedback nuevo
          </h2>
          <p style="font-size:1rem;color:#2E4260;line-height:1.7;margin-bottom:1rem;">
            Hola <strong>{student_name}</strong>, el formador ha revisado tu entrega de la actividad:
          </p>
          <p style="font-size:1.1rem;color:#0F4C81;font-weight:600;margin-bottom:1.5rem;">
            "{task_title}"
          </p>
          <div style="background:#E8F5EC;border-left:4px solid #1A7A52;padding:1.5rem;margin:2rem 0;">
            <h3 style="font-family:var(--font-display);font-size:1.1rem;font-weight:700;color:#1A7A52;margin-bottom:1rem;">
              Feedback del formador:
            </h3>
            <p style="font-size:0.95rem;color:#2E4260;line-height:1.7;white-space:pre-wrap;">
              {feedback.feedback}
            </p>
          </div>
          <p style="font-size:0.9rem;color:#6B82A0;line-height:1.6;">
            Sigue aprendiendo y mejorando. ¡Ya estás más cerca de completar el curso!
          </p>
        """)

        await send_email(
            to_email=student_email,
            subject=f"Tienes feedback nuevo en {task_title}",
            html=html,
        )

    return {"message": "Feedback enviado correctamente"}
