import logging
from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.orm import Session

from dbs.initPostgres import getDatabase
from interfaces.chatInterface import CreateConversationRequest
from services.chatService import ChatService

logger = logging.getLogger(__name__)


class ChatRouter:
    def __init__(self):
        self.router = APIRouter()
        self.router.add_api_route(
            "/createConversation", self.create_conversation, methods=["POST"]
        )
        self.handler = ChatService()

    async def create_conversation(
        self, body: CreateConversationRequest, db: Session = Depends(getDatabase)
    ):
        logger.info("create_conversation called")
        return await self.handler.create_conversation(body, db)
