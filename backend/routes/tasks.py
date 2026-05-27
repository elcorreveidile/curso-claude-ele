"""Task routes: activities, submissions, and feedback."""
from fastapi import APIRouter, Depends, HTTPException

from core import current_admin, current_user, now_utc, send_email, supabase, wrap_email
from models import FeedbackIn, SubmissionIn, SubmissionOut, TaskOut
from seed_content.modules_data import MODULES

router = APIRouter(prefix="/tasks", tags=["tasks"])


def _find_activity(task_id: str):
    for module in MODULES:
        for activity in module.get("activities", []):
            if activity["id"] == task_id:
                return module, activity
    return None, None


@router.get("")
async def get_tasks(user: dict = Depends(current_user)) -> list[TaskOut]:
    """Tasks from accessible modules for the authenticated user."""
    enrollment_id = user["id"]
    progress_result = (
        supabase.table("module_progress")
        .select("*")
        .eq("enrollment_id", enrollment_id)
        .in_("status", ["available", "in_progress", "completed"])
        .execute()
    )
    accessible_ids = {p["module_id"] for p in progress_result.data}

    tasks = []
    for module in MODULES:
        if module["id"] in accessible_ids:
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
async def get_task(task_id: str, user: dict = Depends(current_user)) -> dict:
    """Single task details."""
    module, activity = _find_activity(task_id)
    if not activity:
        raise HTTPException(404, "Actividad no encontrada")
    return {"id": activity["id"], "module_id": module["id"], **activity}


@router.get("/{task_id}/submission")
async def get_submission(task_id: str, user: dict = Depends(current_user)) -> SubmissionOut:
    """Retrieve an existing submission."""
    enrollment_id = user["id"]
    result = (
        supabase.table("task_submissions")
        .select("*")
        .eq("enrollment_id", enrollment_id)
        .eq("activity_id", task_id)
        .execute()
    )
    if not result.data:
        raise HTTPException(404, "No hay entrega para esta actividad")
    sub = result.data[0]
    return SubmissionOut(
        id=sub["id"],
        content=sub["content"],
        submitted_at=sub["submitted_at"],
        feedback=sub.get("feedback"),
        feedback_at=sub.get("feedback_at"),
    )


@router.post("/{task_id}/submit")
async def submit_task(task_id: str, submission: SubmissionIn, user: dict = Depends(current_user)) -> dict:
    """Submit an activity."""
    enrollment_id = user["id"]
    module, activity = _find_activity(task_id)
    if not activity:
        raise HTTPException(404, "Actividad no encontrada")

    result = (
        supabase.table("task_submissions")
        .insert({
            "enrollment_id": enrollment_id,
            "activity_id": task_id,
            "module_id": module["id"],
            "content": submission.content,
            "submitted_at": now_utc().isoformat(),
        })
        .execute()
    )
    if not result.data:
        raise HTTPException(500, "Error al crear entrega")
    return {"message": "Actividad entregada correctamente"}


@router.post("/{task_id}/feedback")
async def give_feedback(task_id: str, feedback: FeedbackIn, admin: dict = Depends(current_admin)) -> dict:
    """Add formador feedback to a submission (admin only)."""
    result = (
        supabase.table("task_submissions")
        .select("*")
        .eq("activity_id", task_id)
        .execute()
    )
    if not result.data:
        raise HTTPException(404, "Entrega no encontrada")

    submission = result.data[0]
    supabase.table("task_submissions").update({
        "feedback": feedback.feedback,
        "feedback_at": now_utc().isoformat(),
    }).eq("id", submission["id"]).execute()

    # Notify student by email
    enrollment = supabase.table("enrollments").select("*").eq("id", submission["enrollment_id"]).execute()
    if enrollment.data:
        student = enrollment.data[0]
        _, activity = _find_activity(task_id)
        task_title = activity["title"] if activity else task_id

        html = wrap_email(f"""
          <h2 style="font-family:sans-serif;font-size:1.5rem;font-weight:800;color:#0F4C81;margin-bottom:1rem;">
            Tienes feedback nuevo
          </h2>
          <p style="font-size:1rem;color:#2E4260;line-height:1.7;margin-bottom:1rem;">
            Hola <strong>{student.get('name', 'Estudiante')}</strong>, el formador ha revisado tu entrega de:
          </p>
          <p style="font-size:1.1rem;color:#0F4C81;font-weight:600;margin-bottom:1.5rem;">
            "{task_title}"
          </p>
          <div style="background:#E8F5EC;border-left:4px solid #1A7A52;padding:1.5rem;margin:2rem 0;">
            <h3 style="font-family:sans-serif;font-size:1.1rem;font-weight:700;color:#1A7A52;margin-bottom:1rem;">
              Feedback del formador:
            </h3>
            <p style="font-size:0.95rem;color:#2E4260;line-height:1.7;white-space:pre-wrap;">
              {feedback.feedback}
            </p>
          </div>
        """)
        await send_email(
            to_email=student["email"],
            subject=f"Tienes feedback nuevo en {task_title}",
            html=html,
        )

    return {"message": "Feedback enviado correctamente"}
