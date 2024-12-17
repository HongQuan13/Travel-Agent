from datetime import datetime
from typing import List, Literal
from pydantic import BaseModel


class CreateConversationRequest(BaseModel):
    user_id: int


class CreateConversationResponse(BaseModel):
    conversation_id: int
    user_id: int


class SenderType:
    bot = "bot"
    user = "user"


class SendMessageRequest(BaseModel):
    conversation_id: int
    user_id: int
    message_text: str


class SendMessageResponse(BaseModel):
    message_id: int
    message_text: str
    conversation_id: int
    sender: Literal["user", "bot"]
    bot_response: str


class MessageInfo(BaseModel):
    sender: str
    message_text: str
    timestamp: datetime
    category: Literal["text", "plan"]


class RetrieveConversationResponse(BaseModel):
    all_messages: List[MessageInfo]
