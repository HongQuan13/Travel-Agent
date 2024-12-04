import logging
from fastapi import HTTPException
from sqlalchemy.orm import Session

from models.user_model import User
from models.conversation_model import Conversation
from models.message_model import Message
from interfaces.chat_interface import (
    CreateConversationResponse,
    CreateConversationRequest,
    SendMessageRequest,
    SendMessageResponse,
    SenderType,
)
from travel_agent.agent_manager import AgentManager


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

    async def send_message(self, message: SendMessageRequest, db: Session):
        exist_user = db.query(User).filter_by(id=message.user_id).first()
        if not exist_user:
            raise HTTPException(status_code=400, detail="User account not exist")

        exist_conversation = (
            db.query(Conversation).filter_by(id=message.conversation_id).first()
        )
        if not exist_conversation:
            raise HTTPException(status_code=400, detail="Conversation not exist")

        new_message = Message(
            conversation_id=message.conversation_id,
            sender=SenderType.user,
            message_text=message.message_text,
        )
        db.add(new_message)
        db.commit()
        logger.info(
            f"Send new message to conversation {message.conversation_id} successfully"
        )

        return SendMessageResponse(
            message_id=new_message.id,
            message_text=new_message.message_text,
            sender=SenderType.user,
            conversation_id=message.conversation_id,
        )

    async def bot_reply(self, db: Session):
        llm = AgentManager()
        chat_response = llm.generate_response(user_input=..., conversation_id=...)
