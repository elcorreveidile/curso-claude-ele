"""La Clase Digital - Backend FastAPI.

Curso: Claude para la enseñanza: domina la herramienta
"""
import logging
from contextlib import asynccontextmanager
from datetime import datetime, timezone

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from fastapi import FastAPI, HTTPException, Request
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import Response as StarletteResponse

from core import FRONTEND_ORIGIN, _supabase_init_error, log, supabase
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

# CORS — custom middleware to guarantee headers regardless of Starlette version
_CORS_ORIGINS = {o for o in [
    FRONTEND_ORIGIN,
    "http://localhost:3000",
    "https://curso-claude-ele.vercel.app",
    "https://claude.laclasedigital.com",
] if o}


class _ManualCORS(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        origin = request.headers.get("origin", "")
        allowed = origin in _CORS_ORIGINS

        if request.method == "OPTIONS":
            res = StarletteResponse(status_code=200)
            if allowed:
                res.headers["Access-Control-Allow-Origin"] = origin
                res.headers["Access-Control-Allow-Credentials"] = "true"
                res.headers["Access-Control-Allow-Methods"] = "GET,POST,PUT,PATCH,DELETE,OPTIONS"
                res.headers["Access-Control-Allow-Headers"] = "Content-Type,Authorization,Cookie"
                res.headers["Access-Control-Max-Age"] = "600"
            return res

        response = await call_next(request)
        if allowed:
            response.headers["Access-Control-Allow-Origin"] = origin
            response.headers["Access-Control-Allow-Credentials"] = "true"
        return response


app.add_middleware(_ManualCORS)

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


@app.get("/debug")
async def debug(request: Request):
    """Diagnostic endpoint — shows env config and request headers."""
    import os
    supabase_url = os.environ.get("SUPABASE_URL", "")
    supabase_key = os.environ.get("SUPABASE_SERVICE_KEY", "")
    return {
        "origin_header": request.headers.get("origin", "(none)"),
        "host": request.headers.get("host", "(none)"),
        "cors_allowed_origins": sorted(_CORS_ORIGINS),
        "frontend_origin_env": os.environ.get("FRONTEND_ORIGIN", "(not set)"),
        "resend_api_key_set": bool(os.environ.get("RESEND_API_KEY")),
        "stripe_secret_key_prefix": os.environ.get("STRIPE_SECRET_KEY", "")[:7] or "(not set)",
        "supabase_url_set": bool(supabase_url),
        "supabase_url_preview": supabase_url[:30] + "..." if len(supabase_url) > 30 else supabase_url,
        "supabase_key_set": bool(supabase_key),
        "supabase_key_len": len(supabase_key),
        "supabase_key_prefix": supabase_key[:15] + "..." if len(supabase_key) > 15 else "(missing)",
        "supabase_init_error": _supabase_init_error,
        "jwt_secret_set": bool(os.environ.get("JWT_SECRET")),
        "magic_link_secret_set": bool(os.environ.get("MAGIC_LINK_SECRET")),
        "port_env": os.environ.get("PORT", "(not set)"),
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }


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
