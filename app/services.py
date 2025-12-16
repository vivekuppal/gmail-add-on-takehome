from .models import EmailAddonRequest


async def build_display_text(req: EmailAddonRequest) -> str:
    to_preview = ", ".join(req.to[:3]) + ("..." if len(req.to) > 3 else "")
    bcc_preview = ", ".join(req.bcc[:3]) + ("..." if len(req.bcc) > 3 else "")

    body = req.body_text or ""
    body_snippet = (body[:240] + "…") if len(body) > 240 else body

    lines = [
        "Email Add-on Analysis",
        f"From: {req.frm or '(unknown)'}",
        f"To: {to_preview or '(none)'}",
        f"Bcc: {bcc_preview or '(none)'}",
        f"Subject: {req.subject or '(none)'}",
        "",
        "Snippet:",
        body_snippet or "(no body_text provided)",
    ]
    return "\n".join(lines)
