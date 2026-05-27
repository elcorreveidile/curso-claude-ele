"""La Clase Digital - Backend FastAPI.

Curso: Claude para la enseñanza: domina la herramienta
"""
import logging
from contextlib import asynccontextmanager
from datetime import datetime, timezone

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from core import FRONTEND_ORIGIN, log, supabase
from routes import admin, auth, certificates, modules, payments, tasks

# ─────────────────────────── Lifespan ────────────────────────────
scheduler = AsyncIOScheduler()


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Startup and shutdown events."""
    # Startup
    scheduler.start()
    log.info("Scheduler started")

    yield

    # Shutdown
    scheduler.shutdown()
    log.info("Scheduler shutdown")


# ─────────────────────────── App ─────────────────────────────────
app = FastAPI(
    title="Claude para la enseñanza - API",
    description="Backend del curso de formación docente sobre Claude",
    version="1.0.0",
    lifespan=lifespan,
)

# CORS
# Allow both custom domain and Vercel preview URL
allowed_origins = [
    FRONTEND_ORIGIN,
    "http://localhost:3000",
    "https://curso-claude-ele.vercel.app",
    "https://claude.laclasedigital.com",
]
# Remove duplicates and empty strings
allowed_origins = list(set([o for o in allowed_origins if o]))

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router)
app.include_router(payments.router)
app.include_router(modules.router)
app.include_router(tasks.router)
app.include_router(admin.router)
app.include_router(certificates.router)


# ─────────────────────────── Root ───────────────────────────────
@app.get("/")
async def root():
    return {
        "message": "Claude para la enseñanza - API",
        "version": "1.0.0",
        "docs": "/docs",
    }


@app.get("/health")
async def health():
    """Health check endpoint."""
    return {"status": "healthy", "timestamp": datetime.now(timezone.utc).isoformat()}


# ─────────────────────────── Scheduled Tasks ───────────────────
@scheduler.scheduled_job("cron", hour="*", minute="0")  # Every hour
async def check_upcoming_sessions():
    """Check for upcoming live sessions and send reminders."""
    try:
        # Get sessions scheduled in next 24 hours
        now = datetime.now(timezone.utc)
        tomorrow = now.replace(hour=now.hour + 24)

        result = supabase.table("live_sessions").select("*").gte("scheduled_at", now.isoformat()).lt("scheduled_at", tomorrow.isoformat()).eq("status", "scheduled").execute()

        for session in result.data:
            # Send reminder email to all active enrollments
            enrollments = supabase.table("enrollments").select("email, name").eq("status", "active").execute()

            for enrollment in enrollments.data:
                # TODO: Send reminder email
                log.info(f"Reminder sent to {enrollment['email']} for session {session['title']}")

    except Exception as e:
        log.error(f"Error checking upcoming sessions: {e}")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
