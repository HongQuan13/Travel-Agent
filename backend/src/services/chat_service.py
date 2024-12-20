import json
import logging
from fastapi import HTTPException
from sqlalchemy.orm import Session

from backend.src.models.itinerary_model import Itinerary
from backend.src.models.user_model import User
from backend.src.models.conversation_model import Conversation
from backend.src.models.message_model import Message
from backend.src.interfaces.chat_interface import (
    CreateConversationResponse,
    CreateConversationRequest,
    MessageInfo,
    RetrieveConversationResponse,
    RetrieveItineraryDetailResponse,
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

    async def send_message(
        self, message: SendMessageRequest, user_id: int, db: Session
    ):
        exist_user = db.query(User).filter_by(id=user_id).first()
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
            content=message.content,
        )
        db.add(new_message)
        db.commit()
        logger.info(
            f"Send new message to conversation {message.conversation_id} successfully"
        )

        bot_response = await self.bot_reply(
            message.content, message.conversation_id, db
        )

        return SendMessageResponse(
            message_id=new_message.id,
            content=new_message.content,
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
            content=chat_response,
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
            db.query(
                Message.content,
                Message.timestamp,
                Message.sender,
                Message.category,
            )
            .filter(Message.conversation_id == conversation_id)
            .order_by(Message.timestamp)
            .all()
        )

        structured_messages = [
            MessageInfo(
                content=m[0],
                timestamp=m[1],
                sender=m[2],
                category=(m[3] if m[3] != None else "text"),
            )
            for m in all_messages
        ]

        return RetrieveConversationResponse(all_messages=structured_messages)

    async def retrieve_itinerary(self, itinerary_id: int, db: Session):
        itinerary_content = (
            db.query(Itinerary.itinerary_detail).filter_by(id=itinerary_id).first()
        )

        if not itinerary_content:
            raise HTTPException(status_code=400, detail="Itinerary not exist")

        return RetrieveItineraryDetailResponse(itinerary_detail=itinerary_content[0])

    async def retrieve_latest_itinerary(self, conversation_id: int, db: Session):
        exist_conversation = (
            db.query(Conversation).filter_by(id=conversation_id).first()
        )

        if not exist_conversation:
            raise HTTPException(status_code=400, detail="Conversation not exist")

        itinerary_id = (
            db.query(Message.content)
            .filter(
                Message.conversation_id == conversation_id,
                Message.sender == "bot",
                Message.category == "itinerary",
            )
            .order_by(Message.timestamp.desc())
            .first()
        )
        itinerary_content = (
            db.query(Itinerary.itinerary_detail).filter_by(id=itinerary_id[0]).first()
        )

        if not itinerary_content:
            raise HTTPException(status_code=400, detail="itinerary not exist")

        return RetrieveItineraryDetailResponse(itinerary_detail=itinerary_content[0])
