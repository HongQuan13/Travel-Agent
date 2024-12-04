import logging
from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.orm import Session

from dbs.init_postgres import get_database
from interfaces.chat_interface import CreateConversationRequest
from services.chat_service import ChatService

logger = logging.getLogger(__name__)


class ChatRouter:
    def __init__(self):
        self.router = APIRouter()
        self.router.add_api_route(
            "/create-conversation", self.create_conversation, methods=["POST"]
        )
        self.handler = ChatService()

    async def create_conversation(
        self, body: CreateConversationRequest, db: Session = Depends(get_database)
    ):
        logger.info("create_conversation called")
        return await self.handler.create_conversation(body, db)
