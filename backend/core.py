"""Shared core: config, DB, helpers, email, JWT, FastAPI deps.

This module owns the side-effecting bootstrapping (env loading, DB client,
Stripe SDK). Other modules import names from here rather than
re-running setup.
"""
from __future__ import annotations

import logging
import os
import secrets
import uuid
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Optional

import httpx
from dotenv import load_dotenv
from fastapi import Depends, Header, HTTPException
from jose import JWTError, jwt
from supabase import create_client

import stripe as stripe_sdk

# ─────────────────────────── Config ────────────────────────────
ROOT = Path(__file__).parent
load_dotenv(ROOT / ".env")

SUPABASE_URL = os.environ["SUPABASE_URL"]
SUPABASE_SERVICE_KEY = os.environ["SUPABASE_SERVICE_KEY"]
JWT_SECRET = os.environ["JWT_SECRET"]
MAGIC_LINK_SECRET = os.environ["MAGIC_LINK_SECRET"]
STRIPE_SECRET_KEY = os.environ.get("STRIPE_SECRET_KEY", "sk_test_emergent")
RESEND_API_KEY = os.environ.get("RESEND_API_KEY", "")
RESEND_DISABLE = os.environ.get("RESEND_DISABLE", "0") == "1"
RESEND_FROM = os.environ.get("RESEND_FROM", "curso@laclasedigital.com")
RESEND_FROM_NAME = os.environ.get("RESEND_FROM_NAME", "La Clase Digital")
RESEND_REPLY_TO = os.environ.get("RESEND_REPLY_TO", "")
ADMIN_EMAIL = os.environ.get("ADMIN_EMAIL", "benitezl@go.ugr.es")
FRONTEND_ORIGIN = os.environ.get("FRONTEND_ORIGIN", "").rstrip("/")

stripe_sdk.api_key = STRIPE_SECRET_KEY

logging.basicConfig(level=logging.INFO)
log = logging.getLogger("claude-curso")

# ─────────────────────────── DB (Supabase) ─────────────────────
supabase = create_client(SUPABASE_URL, SUPABASE_SERVICE_KEY)


# ─────────────────────────── Helpers ───────────────────────────
def new_id() -> str:
    return str(uuid.uuid4())


def now_utc() -> datetime:
    return datetime.now(timezone.utc)


def iso(dt: Optional[datetime]) -> Optional[str]:
    """Serialise a datetime to ISO-8601 with timezone info."""
    if dt is None:
        return None
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.isoformat()


def clean_row(row: Optional[dict]) -> Optional[dict]:
    """Remove Supabase metadata and convert datetimes to ISO strings."""
    if not row:
        return row
    out = {k: v for k, v in row.items() if k not in ["id", "_ab1"]}
    for k, v in list(out.items()):
        if isinstance(v, datetime):
            if v.tzinfo is None:
                v = v.replace(tzinfo=timezone.utc)
            out[k] = v.isoformat()
    return out


# ─────────────────────────── Email (Resend) ───────────────────
async def send_email(
    to_email: str,
    subject: str,
    html: str,
    attachments: Optional[list[dict]] = None,
) -> None:
    """Send a transactional email via Resend."""
    if RESEND_DISABLE:
        log.info("RESEND_DISABLE=1 → skipping real email to %s (subject: %s)", to_email, subject)
        return
    if not RESEND_API_KEY:
        log.warning("RESEND_API_KEY missing, skipping email to %s", to_email)
        return
    if "@" not in RESEND_FROM or RESEND_FROM.strip().endswith("@"):
        log.error(
            "RESEND_FROM is malformed (%r) — must be a full email address like "
            "'curso@laclasedigital.com'. Skipping send to %s.",
            RESEND_FROM, to_email,
        )
        raise RuntimeError(
            f"RESEND_FROM está mal configurado: '{RESEND_FROM}'. Debe ser una "
            "dirección completa, p. ej. curso@laclasedigital.com"
        )
    payload: dict[str, Any] = {
        "from": f"{RESEND_FROM_NAME} <{RESEND_FROM}>",
        "to": [to_email],
        "subject": subject,
        "html": html,
    }
    if RESEND_REPLY_TO:
        payload["reply_to"] = RESEND_REPLY_TO
    if attachments:
        payload["attachments"] = [
            {
                "filename": a["filename"],
                "content": a["content_b64"],
                **({"content_type": a["content_type"]} if a.get("content_type") else {}),
            }
            for a in attachments
        ]
    try:
        async with httpx.AsyncClient(timeout=20) as client:
            r = await client.post(
                "https://api.resend.com/emails",
                headers={
                    "Authorization": f"Bearer {RESEND_API_KEY}",
                    "Content-Type": "application/json",
                },
                json=payload,
            )
            if r.status_code >= 300:
                log.error("Resend error %s: %s", r.status_code, r.text)
            else:
                log.info("Email sent to %s", to_email)
    except Exception as exc:
        log.exception("Email failure: %s", exc)


EMAIL_FOOTER = (
    '<hr style="border:none;border-top:1px solid #E8EEF5;margin:24px 0">'
    '<p style="font-size:12px;color:#6B82A0;font-family:Georgia,serif">'
    '<span style="opacity:.9">[|]</span> Claude para la enseñanza · '
    'Formación docente · '
    '<a href="https://claude.laclasedigital.com" style="color:#0F4C81">claude.laclasedigital.com</a></p>'
)


def wrap_email(inner: str) -> str:
    """Wrap an inner HTML fragment in a mobile-friendly email shell."""
    return (
        '<!DOCTYPE html><html lang="es"><head>'
        '<meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width,initial-scale=1">'
        '<meta name="x-apple-disable-message-reformatting">'
        '<style>'
        'body{margin:0;padding:0;background:#F4F7FA;'
        '-webkit-text-size-adjust:100%;-ms-text-size-adjust:100%}'
        '@media only screen and (max-width:600px){'
        '.elc-wrap{padding:18px 16px !important;max-width:100% !important}'
        '.elc-wrap p,.elc-wrap li,.elc-wrap td{font-size:16px !important;line-height:1.6 !important}'
        '.elc-wrap h1{font-size:24px !important;line-height:1.25 !important}'
        '.elc-wrap h2{font-size:22px !important;line-height:1.3 !important}'
        '.elc-wrap h3{font-size:18px !important;line-height:1.3 !important}'
        '.elc-wrap a.elc-btn{display:block !important;padding:16px 22px !important;'
        'font-size:17px !important;text-align:center !important}'
        '}'
        '</style>'
        '</head><body>'
        '<div class="elc-wrap" style="font-family:system-ui,-apple-system,BlinkMacSystemFont,'
        '\'Segoe UI\',sans-serif;max-width:600px;margin:0 auto;padding:24px;color:#1A2535;'
        'font-size:16px;line-height:1.6;background:#FFFFFF">'
        + inner
        + EMAIL_FOOTER
        + "</div></body></html>"
    )


# ─────────────────────────── Auth ──────────────────────────────
def create_session_jwt(user_id: str, email: str, role: str = "student") -> str:
    payload = {
        "sub": user_id,
        "email": email,
        "role": role,
        "iat": int(now_utc().timestamp()),
        "exp": int((now_utc() + timedelta(days=30)).timestamp()),
    }
    return jwt.encode(payload, JWT_SECRET, algorithm="HS256")


def create_magic_token(
    email: str,
    expires_in: timedelta = timedelta(minutes=30),
) -> str:
    payload = {
        "email": email.lower(),
        "purpose": "magic_link",
        "iat": int(now_utc().timestamp()),
        "exp": int((now_utc() + expires_in).timestamp()),
        "nonce": secrets.token_urlsafe(16),
    }
    return jwt.encode(payload, MAGIC_LINK_SECRET, algorithm="HS256")


def verify_magic_token(token: str) -> str:
    """Returns email."""
    try:
        data = jwt.decode(token, MAGIC_LINK_SECRET, algorithms=["HS256"])
    except JWTError as exc:
        raise HTTPException(400, "Enlace inválido o caducado") from exc
    if data.get("purpose") != "magic_link":
        raise HTTPException(400, "Token inválido")
    return data["email"]


async def current_user_optional(
    authorization: Optional[str] = Header(None),
) -> Optional[dict]:
    if not authorization or not authorization.lower().startswith("bearer "):
        return None
    token = authorization.split(" ", 1)[1]
    try:
        data = jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
    except JWTError:
        return None
    # Fetch user from Supabase
    result = supabase.table("enrollments").select("*").eq("id", data["sub"]).execute()
    if result.data:
        user = result.data[0]
        # Update last_seen_at (throttled to 5 min)
        try:
            prev = user.get("last_seen_at")
            now = now_utc()
            should_write = True
            if isinstance(prev, str):
                prev = datetime.fromisoformat(prev)
                if prev.tzinfo is None:
                    prev = prev.replace(tzinfo=timezone.utc)
                should_write = (now - prev).total_seconds() > 300
            if should_write:
                supabase.table("enrollments").update({"last_seen_at": now.isoformat()}).eq("id", user["id"]).execute()
                user["last_seen_at"] = now.isoformat()
        except Exception as exc:
            log.warning("last_seen_at touch skipped: %s", exc)
        return clean_row(user)
    return None


async def current_user(
    authorization: Optional[str] = Header(None),
) -> dict:
    user = await current_user_optional(authorization)
    if not user:
        raise HTTPException(401, "No autenticado")
    return user


async def current_admin(user: dict = Depends(current_user)) -> dict:
    if user.get("role") != "admin":
        raise HTTPException(403, "Acceso restringido")
    return user
