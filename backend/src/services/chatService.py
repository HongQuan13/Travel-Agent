import logging
from sqlalchemy.orm import Session

from models.conversationModel import Conversation
from interfaces.chatInterface import (
    CreateConversationResponse,
    CreateConversationRequest,
)


logger = logging.getLogger(__name__)


class ChatService:
    def __init__(self):
        logger.info("ChatService initialized")

    async def create_conversation(self, user: CreateConversationRequest, db: Session):
        newConversation = Conversation(user_id=user.user_id)
        db.add(newConversation)
        db.commit()
        logger.info(f"Create new new conversation for {user.user_id} successfully")
        return CreateConversationResponse(
            conversation_id=newConversation.id, user_id=user.user_id
        )
