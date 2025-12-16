import email.utils
from typing import List, Optional
from .models import GmailAddonEvent, EmailAddonRequest


def _parse_address_list(value: Optional[str]) -> List[str]:
    """
    Converts:
      'Bob <bob@a.com>, alice@b.com'
    into:
      ['bob@a.com', 'alice@b.com']
    """
    if not value:
        return []

    parsed = email.utils.getaddresses([value])
    return [addr for _, addr in parsed if addr]


def extract_normalized_email(event: GmailAddonEvent) -> EmailAddonRequest:
    gmail = event.gmail
    meta = gmail.messageMetadata if gmail else None

    return EmailAddonRequest(
        message_id=gmail.messageId if gmail else None,
        frm=email.utils.parseaddr(meta.from_)[1] if meta and meta.from_ else None,
        to=_parse_address_list(meta.to if meta else None),
        cc=_parse_address_list(meta.cc if meta else None),
        bcc=_parse_address_list(meta.bcc if meta else None),
        subject=meta.subject if meta else None,
        body_text=gmail.messageText if gmail else None,
        body_html=gmail.messageHtml if gmail else None,
    )
