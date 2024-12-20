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
    content: str


class SendMessageResponse(BaseModel):
    message_id: int
    content: str
    conversation_id: int
    sender: Literal["user", "bot"]
    bot_response: str


class MessageInfo(BaseModel):
    sender: str
    content: str
    timestamp: datetime
    category: Literal["text", "itinerary"]


class RetrieveConversationResponse(BaseModel):
    all_messages: List[MessageInfo]


class RetrieveItineraryDetailResponse(BaseModel):
    itinerary_detail: str
