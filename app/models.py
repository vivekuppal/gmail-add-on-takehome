from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any


class EmailAddonRequest(BaseModel):
    message_id: Optional[str] = None

    to: List[str] = Field(default_factory=list)
    frm: Optional[str] = Field(default=None, alias="from")
    cc: List[str] = Field(default_factory=list)
    bcc: List[str] = Field(default_factory=list)

    subject: Optional[str] = None
    body_text: Optional[str] = None
    body_html: Optional[str] = None

    # optional passthrough for add-on metadata
    meta: Dict[str, Any] = Field(default_factory=dict)

    model_config = {
        "populate_by_name": True  # allows "from" in JSON to map to frm
    }


class EmailAddonResponse(BaseModel):
    text: str


class CommonEventObject(BaseModel):
    hostApp: Optional[str] = None
    userLocale: Optional[str] = None
    userEmail: Optional[str] = None


class GmailMessageMetadata(BaseModel):
    from_: Optional[str] = None
    to: Optional[str] = None
    cc: Optional[str] = None
    bcc: Optional[str] = None
    subject: Optional[str] = None

    class Config:
        fields = {"from_": "from"}


class GmailObject(BaseModel):
    messageId: Optional[str] = None
    threadId: Optional[str] = None
    accessToken: Optional[str] = None
    messageMetadata: Optional[GmailMessageMetadata] = None
    messageText: Optional[str] = None
    messageHtml: Optional[str] = None


class GmailAddonEvent(BaseModel):
    commonEventObject: Optional[CommonEventObject] = None
    gmail: Optional[GmailObject] = None
