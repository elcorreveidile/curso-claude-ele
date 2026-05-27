"""Payment routes: Stripe Checkout + Webhooks."""
import os
import stripe as stripe_sdk
from fastapi import APIRouter, HTTPException, Request, Header
from fastapi.responses import JSONResponse

from core import (
    ADMIN_EMAIL,
    BACKEND_URL,
    FRONTEND_ORIGIN,
    create_magic_token,
    send_email,
    supabase,
    wrap_email,
)
from models import CheckoutRequest
from seed_content.modules_data import MODULES, MODULE_UNLOCK_RULES

router = APIRouter(prefix="/payments", tags=["payments"])

STRIPE_PRICE_ID = os.environ.get("STRIPE_PRICE_ID_CURSO_CLAUDE", "PENDIENTE_DE_CONFIGURAR")


@router.post("/create-checkout-session")
async def create_checkout_session(checkout_data: CheckoutRequest) -> dict:
    """Create Stripe Checkout session."""
    try:
        # Check if email already enrolled
        result = supabase.table("enrollments").select("*").eq("email", checkout_data.email.lower()).execute()

        if result.data:
            # User already enrolled - redirect to dashboard
            return {
                "error": "Ya estás inscrito en este curso",
                "redirect_url": f"{FRONTEND_ORIGIN}/dashboard",
            }

        # Create Stripe Checkout session
        session = stripe_sdk.checkout.Session.create(
            payment_method_types=["card"],
            line_items=[
                {
                    "price": STRIPE_PRICE_ID,
                    "quantity": 1,
                }
            ],
            mode="payment",
            success_url=f"{checkout_data.origin_url}/inscripcion/success?session_id={{CHECKOUT_SESSION_ID}}",
            cancel_url=f"{checkout_data.origin_url}/precios?cancelled=true",
            customer_email=checkout_data.email,
            metadata={
                "name": checkout_data.name,
                "email": checkout_data.email,
            },
        )

        return {"checkout_url": session.url}

    except Exception as e:
        raise HTTPException(500, f"Error creating checkout session: {str(e)}")


@router.post("/stripe-webhook")
async def stripe_webhook(request: Request, stripe_signature: str = Header(...)):
    """Handle Stripe webhooks."""
    webhook_secret = os.environ.get("STRIPE_WEBHOOK_SECRET")
    if not webhook_secret:
        raise HTTPException(500, "Webhook secret not configured")

    payload = await request.body()
    sig_header = stripe_signature

    try:
        event = stripe_sdk.Webhook.construct_event(
            payload, sig_header, webhook_secret
        )
    except ValueError as e:
        raise HTTPException(400, "Invalid payload") from e
    except stripe_sdk.error.SignatureVerificationError as e:
        raise HTTPException(400, "Invalid signature") from e

    # Handle checkout.session.completed event
    if event["type"] == "checkout.session.completed":
        session = event["data"]["object"]
        await handle_checkout_session_completed(session)

    return JSONResponse(content={"status": "success"})


async def handle_checkout_session_completed(session: dict):
    """Process successful checkout - create enrollment and send welcome email."""
    metadata = session.get("metadata", {})
    email = metadata.get("email", "").lower()
    name = metadata.get("name", "")
    amount_paid = session.get("amount_total", 14900)

    try:
        # Create enrollment
        enrollment_result = supabase.table("enrollments").insert({
            "email": email,
            "name": name,
            "stripe_payment_id": session.get("payment_intent"),
            "amount_paid": amount_paid,
            "status": "active",
        }).execute()

        if not enrollment_result.data:
            raise HTTPException(500, "Error creating enrollment")

        enrollment_id = enrollment_result.data[0]["id"]

        # Create module progress for all modules
        module_progress_data = []
        for module in MODULES:
            unlock_rule = MODULE_UNLOCK_RULES.get(module["id"])
            status = "locked"

            if unlock_rule == "always_open":
                status = "available"
            elif unlock_rule == "on_enrollment":
                status = "available"

            module_progress_data.append({
                "enrollment_id": enrollment_id,
                "module_id": module["id"],
                "status": status,
            })

        supabase.table("module_progress").insert(module_progress_data).execute()

        # Send welcome email to student — link valid for 7 days
        from datetime import timedelta
        magic_token = create_magic_token(email, expires_in=timedelta(days=7))
        magic_link = f"{FRONTEND_ORIGIN}/api/auth/verify?token={magic_token}"

        html = wrap_email(f"""
          <div style="text-align:center;margin-bottom:2rem;">
            <span style="font-family:Georgia,serif;font-size:3rem;color:#F5A623;letter-spacing:-3px;">
              [|]
            </span>
          </div>
          <h1 style="font-family:var(--font-display);font-size:1.8rem;font-weight:800;color:#0F4C81;margin-bottom:1rem;">
            ¡Bienvenido/a al curso!
          </h1>
          <p style="font-size:1.1rem;color:#2E4260;line-height:1.7;margin-bottom:1.5rem;">
            Hola <strong>{name}</strong>, gracias por inscribirte en
            <strong>Claude para la enseñanza: domina la herramienta</strong>.
          </p>
          <p style="font-size:1rem;color:#2E4260;line-height:1.7;margin-bottom:1.5rem;">
            Tu pago de <strong>{amount_paid / 100:.0f} €</strong> se ha procesado correctamente.
            Ya tienes acceso a la plataforma del curso.
          </p>
          <div style="background:#EDF4FB;border-left:4px solid #0F4C81;padding:1.5rem;margin:2rem 0;">
            <h3 style="font-family:var(--font-display);font-size:1.1rem;font-weight:700;color:#0F4C81;margin-bottom:0.5rem;">
              Próximos pasos
            </h3>
            <ol style="font-size:0.95rem;color:#2E4260;line-height:1.7;padding-left:1.5rem;">
              <li style="margin-bottom:0.5rem;">Accede al curso con el botón de abajo</li>
              <li style="margin-bottom:0.5rem;">Empieza por el <strong>Módulo 0: Bienvenida</strong></li>
              <li style="margin-bottom:0.5rem;">Explora los Módulos I y II, ya disponibles</li>
              <li>Prepárate para la primera videotutoría (fecha pendiente)</li>
            </ol>
          </div>
          <div style="text-align:center;margin:2rem 0;">
            <a href="{magic_link}"
               style="display:inline-block;padding:1rem 2.5rem;background:#F5A623;color:#1A2535;text-decoration:none;border-radius:6px;font-weight:700;font-size:1.1rem;">
              Acceder al curso ahora →
            </a>
          </div>
          <p style="font-size:0.9rem;color:#6B82A0;line-height:1.6;margin-top:2rem;">
            Si tienes cualquier duda, no dudes en contactarnes respondiendo a este email.
          </p>
        """)

        await send_email(
            to_email=email,
            subject="Bienvenido/a al curso · Claude para la enseñanza",
            html=html,
        )

        # Send notification email to admin
        admin_html = wrap_email(f"""
          <h2 style="font-family:var(--font-display);font-size:1.5rem;font-weight:800;color:#0F4C81;margin-bottom:1rem;">
            Nueva inscripción
          </h2>
          <p style="font-size:1rem;color:#2E4260;line-height:1.7;margin-bottom:1rem;">
            Se ha inscrito un nuevo participante en el curso:
          </p>
          <ul style="font-size:0.95rem;color:#2E4260;line-height:1.7;">
            <li><strong>Nombre:</strong> {name}</li>
            <li><strong>Email:</strong> {email}</li>
            <li><strong>Pago:</strong> {amount_paid / 100:.0f} €</li>
            <li><strong>Stripe Payment ID:</strong> {session.get('payment_intent')}</li>
          </ul>
        """)

        await send_email(
            to_email=ADMIN_EMAIL,
            subject=f"Nueva inscripción · {name} · {email}",
            html=admin_html,
        )

    except Exception as e:
        # Log error but don't fail the webhook
        print(f"Error processing checkout session: {e}")
        # TODO: Should retry or notify admin
        pass
