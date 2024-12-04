import logging
from sqlalchemy.orm import Session

from models.conversation_model import Conversation
from interfaces.chat_interface import (
    CreateConversationResponse,
    CreateConversationRequest,
)


logger = logging.getLogger(__name__)


class ChatService:
    def __init__(self):
        logger.info("ChatService initialized")

    async def create_conversation(
        self, conversation: CreateConversationRequest, db: Session
    ):
        new_conversation = Conversation(user_id=conversation.user_id)
        db.add(new_conversation)
        db.commit()
        logger.info(f"Create new conversation for {conversation.user_id} successfully")

        return CreateConversationResponse(
            conversation_id=new_conversation.id, user_id=conversation.user_id
        )