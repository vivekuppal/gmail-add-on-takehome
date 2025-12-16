from fastapi import APIRouter, Header, HTTPException
from app.models import EmailAddonRequest, EmailAddonResponse, GmailAddonEvent
from app.services import build_display_text
from app.settings import settings
from app.extract import extract_normalized_email

router = APIRouter(tags=["addon"])


def _check_api_key(x_api_key: str | None) -> None:
    if not settings.api_key:
        return  # disabled
    if not x_api_key or x_api_key != settings.api_key:
        raise HTTPException(status_code=401, detail="Invalid API key")


@router.get("/health")
async def health():
    return {"ok": True, "env": settings.environment, "app": settings.app_name}


@router.post("/analyze_simple", response_model=EmailAddonResponse)
async def analyze_email(
    payload: EmailAddonRequest,
    x_api_key: str | None = Header(default=None),
):
    print("analyze_email called")
    _check_api_key(x_api_key)

    text = await build_display_text(payload)
    return EmailAddonResponse(text=text)


# We will need to add JWT based auth for production use
@router.post("/v1/gmail/analyze")
async def analyze_gmail_event(event: GmailAddonEvent):
    email = extract_normalized_email(event)

    display_text = (
        "Gmail Add-on Analysis\n"
        f"From: {email.frm}\n"
        f"To: {', '.join(email.to)}\n"
        f"Subject: {email.subject}\n"
    )

    return {
        "text": display_text
    }
