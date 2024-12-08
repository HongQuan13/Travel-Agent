import logging
from fastapi import HTTPException
from sqlalchemy.orm import Session

from backend.src.models.user_model import User
from backend.src.models.conversation_model import Conversation
from backend.src.models.message_model import Message
from backend.src.interfaces.chat_interface import (
    CreateConversationResponse,
    CreateConversationRequest,
    MessageInfo,
    RetrieveConversationResponse,
    SendMessageRequest,
    SendMessageResponse,
    SenderType,
)
from travel_agent.agent_handler.gpt_agent_manager import GPTAgentManager


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

        bot_response = await self.bot_reply(
            message.message_text, message.conversation_id, db
        )
        return SendMessageResponse(
            message_id=new_message.id,
            message_text=new_message.message_text,
            sender=SenderType.user,
            conversation_id=message.conversation_id,
            bot_response=bot_response,
        )

    async def bot_reply(self, user_message: str, conversation_id: int, db: Session):
        llm = GPTAgentManager()
        chat_response = llm.generate_response(
            user_input=user_message, conversation_id=conversation_id
        )

        bot_reply = Message(
            conversation_id=conversation_id,
            sender=SenderType.bot,
            message_text=chat_response,
        )
        db.add(bot_reply)
        db.commit()
        logger.info(f"Bot reply to user conversation {conversation_id} successfully")
        return chat_response

    async def retrieve_conversation(self, conversation_id: int, db: Session):
        exist_conversation = (
            db.query(Conversation).filter_by(id=conversation_id).first()
        )
        if not exist_conversation:
            raise HTTPException(status_code=400, detail="Conversation not exist")

        all_messages = (
            db.query(Message.message_text, Message.timestamp, Message.sender)
            .filter(Message.conversation_id == conversation_id)
            .order_by(Message.timestamp)
            .all()
        )

        structured_messages = [
            MessageInfo(message_text=m[0], timestamp=m[1], sender=m[2])
            for m in all_messages
        ]

        return RetrieveConversationResponse(all_messages=structured_messages)
