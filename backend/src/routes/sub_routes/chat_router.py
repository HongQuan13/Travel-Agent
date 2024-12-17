import logging
from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.orm import Session

from backend.src.dbs.init_postgres import get_database
from backend.src.interfaces.chat_interface import (
    CreateConversationRequest,
    SendMessageRequest,
)
from backend.src.services.chat_service import ChatService

logger = logging.getLogger(__name__)


class ChatRouter:
    def __init__(self):
        self.router = APIRouter()
        self.router.add_api_route(
            "/create-conversation", self.create_conversation, methods=["POST"]
        )
        self.router.add_api_route("/send-message", self.send_messsage, methods=["POST"])
        self.router.add_api_route(
            "/retrieve-plan/{plan_id}",
            self.retrieve_plan,
            methods=["GET"],
        )
        self.router.add_api_route(
            "/retrieve-latest-plan/{conversation_id}",
            self.retrieve_latest_plan,
            methods=["GET"],
        )
        self.router.add_api_route(
            "/retrieve-conversation/{conversation_id}",
            self.retrieve_conversation,
            methods=["GET"],
        )
        self.handler = ChatService()

    async def create_conversation(
        self, body: CreateConversationRequest, db: Session = Depends(get_database)
    ):
        logger.info("create_conversation called")
        return await self.handler.create_conversation(body, db)

    async def send_messsage(
        self, body: SendMessageRequest, db: Session = Depends(get_database)
    ):
        logger.info("send_message called")
        return await self.handler.send_message(body, db)

    async def retrieve_conversation(
        self,
        conversation_id: int,
        db: Session = Depends(get_database),
    ):
        logger.info("retrieve_conversation called")
        return await self.handler.retrieve_conversation(conversation_id, db)

    async def retrieve_plan(
        self,
        plan_id: int,
        db: Session = Depends(get_database),
    ):
        logger.info("retrieve_plan called")
        return await self.handler.retrieve_plan(plan_id, db)

    async def retrieve_latest_plan(
        self,
        conversation_id: int,
        db: Session = Depends(get_database),
    ):
        logger.info("retrieve_latest_plan called")
        return await self.handler.retrieve_latest_plan(conversation_id, db)
