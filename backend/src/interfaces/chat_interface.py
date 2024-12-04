from pydantic import BaseModel


class CreateConversationRequest(BaseModel):
    user_id: int


class CreateConversationResponse(BaseModel):
    conversation_id: int
    user_id: int
