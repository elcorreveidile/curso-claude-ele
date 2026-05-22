"""Authentication routes: magic links + JWT."""
from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import RedirectResponse

from core import (
    BACKEND_URL,
    FRONTEND_ORIGIN,
    create_magic_token,
    create_session_jwt,
    log,
    send_email,
    supabase,
    verify_magic_token,
    wrap_email,
)
from models import LoginRequest, VerifyTokenRequest, UserOut

router = APIRouter(prefix="/auth", tags=["auth"])


@router.get("/test")
async def test_endpoint():
    """Test endpoint to verify auth routes are working."""
    return {"message": "Auth routes working", "BACKEND_URL": BACKEND_URL}


@router.post("/login")
async def login(req: LoginRequest) -> dict:
    """Send magic link email."""
    # Check if user exists in enrollments
    result = supabase.table("enrollments").select("*").eq("email", req.email.lower()).execute()

    if not result.data:
        # User not enrolled - don't reveal this for security
        # Still send email but with different message
        pass

    # Create magic token
    token = create_magic_token(req.email)
    magic_link = f"{BACKEND_URL}/auth/verify?token={token}"
    log.info(f"Magic link generated: {magic_link}")

    # Send email
    html = wrap_email(f"""
      <h2 style="font-family:var(--font-display);font-size:1.5rem;font-weight:800;color:#0F4C81;margin-bottom:1rem;">
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
           style="display:inline-block;padding:1rem 2rem;background:#F5A623;color:#1A2535;text-decoration:none;border-radius:6px;font-weight:700;font-size:1rem;">
          Acceder al curso →
        </a>
      </div>
      <p style="font-size:0.9rem;color:#6B82A0;line-height:1.6;">
        Este enlace caduca en 30 minutos. Si no has solicitado acceso, puedes ignorar este email.
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
    """Verify magic token and redirect to frontend with JWT."""
    log.info(f"verify endpoint called with token: {token[:20]}...")
    try:
        email = verify_magic_token(token)

        # Check if user exists in enrollments
        result = supabase.table("enrollments").select("*").eq("email", email).execute()

        if not result.data:
            # User not enrolled - redirect to pricing
            return RedirectResponse(url=f"{FRONTEND_ORIGIN}/precios?error=not_enrolled")

        enrollment = result.data[0]

        # Create JWT
        jwt_token = create_session_jwt(
            user_id=enrollment["id"],
            email=enrollment["email"],
            role=enrollment.get("role", "student"),
        )

        # Redirect to frontend with JWT in URL fragment (not visible to server)
        return RedirectResponse(url=f"{FRONTEND_ORIGIN}/dashboard#token={jwt_token}")

    except HTTPException:
        # Invalid token - redirect to login with error
        return RedirectResponse(url=f"{FRONTEND_ORIGIN}/login?error=invalid_token")


@router.post("/verify-token")
async def verify_token(req: VerifyTokenRequest) -> dict:
    """Verify JWT and return user info."""
    from core import jwt, JWT_SECRET
    from jose import JWTError

    try:
        payload = jwt.decode(req.token, JWT_SECRET, algorithms=["HS256"])
        user_id = payload.get("sub")

        # Fetch user from Supabase
        result = supabase.table("enrollments").select("*").eq("id", user_id).execute()

        if not result.data:
            raise HTTPException(401, "Usuario no encontrado")

        enrollment = result.data[0]

        return UserOut(
            id=enrollment["id"],
            email=enrollment["email"],
            name=enrollment.get("name"),
            role=enrollment.get("role", "student"),
            created_at=enrollment["created_at"],
        )

    except JWTError as e:
        raise HTTPException(401, "Token inválido") from e


@router.get("/me")
async def get_current_user(current_user: dict = None) -> dict:
    """Get current user from JWT (protected route)."""
    from core import current_user as get_user
    from fastapi import Depends

    user = await get_user()
    return UserOut(
        id=user["id"],
        email=user["email"],
        name=user.get("name"),
        role=user.get("role", "student"),
        created_at=user["created_at"],
    )
