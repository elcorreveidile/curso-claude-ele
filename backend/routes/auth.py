"""Authentication routes: magic links + JWT stored in httpOnly cookie."""
from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import JSONResponse, RedirectResponse

from core import (
    BACKEND_URL,
    FRONTEND_ORIGIN,
    create_magic_token,
    create_session_jwt,
    current_user,
    log,
    send_email,
    supabase,
    verify_magic_token,
    wrap_email,
)
from models import LoginRequest, UserOut

router = APIRouter(prefix="/auth", tags=["auth"])

# Cookie config: SameSite=none+Secure for cross-origin production,
# SameSite=lax for same-site (localhost) development.
_is_prod = FRONTEND_ORIGIN.startswith("https://") and "localhost" not in FRONTEND_ORIGIN
_COOKIE_SECURE = _is_prod
_COOKIE_SAMESITE = "none" if _is_prod else "lax"
_COOKIE_MAX_AGE = 30 * 24 * 3600  # 30 days


def _apply_session_cookie(response, jwt_token: str) -> None:
    response.set_cookie(
        key="session_token",
        value=jwt_token,
        httponly=True,
        secure=_COOKIE_SECURE,
        samesite=_COOKIE_SAMESITE,
        max_age=_COOKIE_MAX_AGE,
        path="/",
    )


def _clear_session_cookie(response) -> None:
    response.delete_cookie(
        key="session_token",
        httponly=True,
        secure=_COOKIE_SECURE,
        samesite=_COOKIE_SAMESITE,
        path="/",
    )


@router.get("/test")
async def test_endpoint():
    return {"message": "Auth routes working", "BACKEND_URL": BACKEND_URL}


@router.post("/login")
async def login(req: LoginRequest) -> dict:
    """Send magic link email."""
    token = create_magic_token(req.email)
    magic_link = f"{BACKEND_URL}/auth/verify?token={token}"
    log.info("Magic link generated for %s", req.email)

    html = wrap_email(f"""
      <h2 style="font-family:sans-serif;font-size:1.5rem;font-weight:800;color:#0F4C81;margin-bottom:1rem;">
        Tu enlace de acceso al curso
      </h2>
      <p style="font-size:1rem;color:#2E4260;line-height:1.7;margin-bottom:1.5rem;">
        Hola, hemos recibido una solicitud de acceso para tu cuenta del curso
        <strong>Claude para la enseñanza</strong>.
      </p>
      <p style="font-size:1rem;color:#2E4260;line-height:1.7;margin-bottom:1.5rem;">
        Haz clic en el siguiente botón para acceder directamente a tu área:
      </p>
      <div style="text-align:center;margin:2rem 0;">
        <a href="{magic_link}"
           style="display:inline-block;padding:1rem 2rem;background:#F5A623;color:#1A2535;
                  text-decoration:none;border-radius:6px;font-weight:700;font-size:1rem;">
          Acceder al curso →
        </a>
      </div>
      <p style="font-size:0.9rem;color:#6B82A0;line-height:1.6;">
        Este enlace caduca en 30 minutos. Si no has solicitado acceso, ignora este email.
      </p>
    """)

    await send_email(
        to_email=req.email,
        subject="Tu enlace de acceso al curso",
        html=html,
    )
    return {"message": "Si el email está registrado, recibirás un enlace de acceso"}


@router.get("/verify")
async def verify_magic_link(request: Request, token: str) -> RedirectResponse:
    """Validate magic token, set httpOnly session cookie, redirect to dashboard."""
    log.info("verify endpoint called, token prefix: %s...", token[:20])
    try:
        email = verify_magic_token(token)

        result = supabase.table("enrollments").select("*").eq("email", email).execute()
        if not result.data:
            return RedirectResponse(url=f"{FRONTEND_ORIGIN}/precios?error=not_enrolled")

        enrollment = result.data[0]
        jwt_token = create_session_jwt(
            user_id=enrollment["id"],
            email=enrollment["email"],
            role=enrollment.get("role", "student"),
        )

        response = RedirectResponse(url=f"{FRONTEND_ORIGIN}/dashboard", status_code=302)
        _apply_session_cookie(response, jwt_token)
        return response

    except HTTPException:
        return RedirectResponse(url=f"{FRONTEND_ORIGIN}/login?error=invalid_token")


@router.post("/logout")
async def logout() -> JSONResponse:
    """Clear session cookie."""
    response = JSONResponse(content={"message": "Sesión cerrada"})
    _clear_session_cookie(response)
    return response


@router.get("/me")
async def get_current_user(user: dict = Depends(current_user)) -> UserOut:
    """Return authenticated user (protected)."""
    return UserOut(
        id=user["id"],
        email=user["email"],
        name=user.get("name"),
        role=user.get("role", "student"),
        created_at=user["created_at"],
    )
