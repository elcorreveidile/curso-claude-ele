"""Certificate routes: student-facing certificate access."""
from fastapi import APIRouter, Depends, HTTPException

from core import current_user, supabase
from models import CertificateOut

router = APIRouter(prefix="/certificates", tags=["certificates"])


@router.get("/my")
async def get_my_certificate(user: dict = Depends(current_user)) -> CertificateOut:
    """Return the authenticated user's certificate."""
    result = (
        supabase.table("certificates")
        .select("*")
        .eq("enrollment_id", user["id"])
        .execute()
    )
    if not result.data:
        raise HTTPException(404, "Certificado no disponible aún")
    cert = result.data[0]
    return CertificateOut(
        name=cert["name"],
        verification_code=cert["verification_code"],
        issued_at=cert["issued_at"],
    )
