import json
import logging
from datetime import datetime
from fastapi import HTTPException
from sqlalchemy import desc
from sqlalchemy.orm import Session

from backend.src.constant.info_constant import InfoDetail
from backend.src.constant.success_constant import SuccessDetail
from backend.src.models.itinerary_model import Itinerary
from backend.src.models.user_model import User
from backend.src.models.conversation_model import Conversation
from backend.src.models.message_model import Message
from backend.src.interfaces.chat_interface import (
    ConversationHistoryResponse,
    ConversationInfo,
    CreateConversationRequest,
    CreateConversationResponse,
    MessageCategory,
    MessageInfo,
    RetrieveConversationResponse,
    RetrieveItineraryDetailResponse,
    SendMessageRequest,
    SendMessageResponse,
    SenderType,
)
from backend.src.constant.error_constant import ErrorDetail
from travel_agent.agent_handler.gpt_agent_manager import GPTAgentManager


logger = logging.getLogger(__name__)


class ChatService:
    def __init__(self):
        logger.info(InfoDetail.class_initialize("ChatService"))

    async def create_conversation(
        self, body: CreateConversationRequest, user_id: int, db: Session
    ):
        llm = GPTAgentManager()
        conversation_title = llm.generate_conversation_title(body.first_message)
        new_conversation = Conversation(user_id=user_id, title=conversation_title)
        db.add(new_conversation)
        db.flush()

        new_message = Message(
            conversation_id=new_conversation.id,
            sender=SenderType.user,
            content=body.first_message,
        )

        db.add(new_message)
        db.commit()

        bot_response = await self.bot_reply(body.first_message, new_conversation.id, db)

        logger.info(SuccessDetail.new_conversation(user_id))

        return CreateConversationResponse(
            conversation_id=new_conversation.id,
            user_id=user_id,
            bot_response=bot_response,
            conversation_title=conversation_title,
        )

    async def conversation_history(self, user_id: int, db: Session):
        exist_user = db.query(User).filter_by(id=user_id).first()
        if not exist_user:
            raise HTTPException(status_code=400, detail=ErrorDetail.non_exist_user)

        conversation_list = (
            db.query(
                Conversation.id,
                Conversation.title,
                db.query(Message.timestamp)
                .filter(Message.conversation_id == Conversation.id)
                .order_by(Message.timestamp.desc())
                .limit(1)
                .label("last_update_at"),
                db.query(Message.content)
                .filter(Message.conversation_id == Conversation.id)
                .filter(Message.sender == "user")
                .order_by(Message.timestamp.desc())
                .limit(1)
                .label("last_user_message"),
            )
            .filter(Conversation.user_id == user_id)
            .order_by(desc("last_update_at"))
            .all()
        )

        structured_conversations = [
            ConversationInfo(
                conversation_id=c[0],
                conversation_title=c[1],
                updated_at=c[2] if c[2] else datetime.min,
                last_user_message=c[3],
            )
            for c in conversation_list
        ]

        logger.info(SuccessDetail.all_conversation(user_id))

        return ConversationHistoryResponse(conversations=structured_conversations)

    async def send_message(
        self, message: SendMessageRequest, user_id: int, db: Session
    ):
        exist_user = db.query(User).filter_by(id=user_id).first()
        if not exist_user:
            raise HTTPException(status_code=400, detail=ErrorDetail.non_exist_user)

        exist_conversation = (
            db.query(Conversation).filter_by(id=message.conversation_id).first()
        )
        if not exist_conversation:
            raise HTTPException(
                status_code=400, detail=ErrorDetail.non_exist_conversation
            )

        new_message = Message(
            conversation_id=message.conversation_id,
            sender=SenderType.user,
            content=message.content,
        )
        db.add(new_message)
        db.commit()
        logger.info(SuccessDetail.new_message(message.conversation_id))

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
            user_input=user_message, conversation_id=str(conversation_id)
        )

        bot_reply = Message(
            conversation_id=conversation_id,
            sender=SenderType.bot,
            content=chat_response,
        )
        db.add(bot_reply)
        db.commit()
        logger.info(SuccessDetail.bot_reply_message(conversation_id))
        return chat_response

    async def retrieve_conversation(self, conversation_id: int, db: Session):
        exist_conversation = (
            db.query(Conversation).filter_by(id=conversation_id).first()
        )
        if not exist_conversation:
            raise HTTPException(
                status_code=400, detail=ErrorDetail.non_exist_conversation
            )

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
                category=(m[3] if m[3] != None else MessageCategory.text),
            )
            for m in all_messages
        ]

        return RetrieveConversationResponse(all_messages=structured_messages)

    async def retrieve_itinerary(self, itinerary_id: int, db: Session):
        itinerary_content = (
            db.query(Itinerary.itinerary_detail).filter_by(id=itinerary_id).first()
        )

        if not itinerary_content:
            raise HTTPException(status_code=400, detail=ErrorDetail.non_exist_itinerary)

        return RetrieveItineraryDetailResponse(
            itinerary_detail=json.loads(itinerary_content[0])
        )

    async def retrieve_latest_itinerary(self, conversation_id: int, db: Session):
        exist_conversation = (
            db.query(Conversation).filter_by(id=conversation_id).first()
        )

        if not exist_conversation:
            raise HTTPException(
                status_code=400, detail=ErrorDetail.non_exist_conversation
            )

        itinerary_id = (
            db.query(Message.content)
            .filter(
                Message.conversation_id == conversation_id,
                Message.sender == SenderType.bot,
                Message.category == MessageCategory.itinerary,
            )
            .order_by(Message.timestamp.desc())
            .first()
        )

        if itinerary_id == None or len(itinerary_id) == 0:
            return None

        itinerary_content = (
            db.query(Itinerary.itinerary_detail).filter_by(id=itinerary_id[0]).first()
        )

        if not itinerary_content:
            raise HTTPException(status_code=400, detail=ErrorDetail.non_exist_itinerary)

        return RetrieveItineraryDetailResponse(
            itinerary_detail=json.loads(itinerary_content[0])
        )
