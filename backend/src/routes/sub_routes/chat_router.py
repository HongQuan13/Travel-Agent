import logging
from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.orm import Session

from backend.src.constant.info_constant import InfoDetail
from backend.src.dbs.init_postgres import get_database
from backend.src.interfaces.chat_interface import (
    CreateConversationRequest,
    SendMessageRequest,
)
from backend.src.services.auth_service import AuthService
from backend.src.services.chat_service import ChatService

logger = logging.getLogger(__name__)


class ChatRouter:
    def __init__(self):
        self.router = APIRouter()
        self.router.add_api_route(
            "/create-conversation", self.create_conversation, methods=["POST"]
        )
        self.router.add_api_route(
            "/conversation-history", self.conversation_history, methods=["GET"]
        )
        self.router.add_api_route("/send-message", self.send_messsage, methods=["POST"])
        self.router.add_api_route(
            "/retrieve-itinerary/{itinerary_id}",
            self.retrieve_itinerary,
            methods=["GET"],
        )
        self.router.add_api_route(
            "/retrieve-latest-itinerary/{conversation_id}",
            self.retrieve_latest_itinerary,
            methods=["GET"],
        )
        self.router.add_api_route(
            "/retrieve-conversation/{conversation_id}",
            self.retrieve_conversation,
            methods=["GET"],
        )
        self.handler = ChatService()

    async def create_conversation(
        self,
        body: CreateConversationRequest,
        user_info: dict = Depends(AuthService().verify_jwt_token),
        db: Session = Depends(get_database),
    ):
        logger.info(InfoDetail.func_call("create_conversation"))
        user_id = user_info["id"]
        print("testttt", user_id, type(user_id))
        return await self.handler.create_conversation(body, user_id, db)

    async def conversation_history(
        self,
        user_info: dict = Depends(AuthService().verify_jwt_token),
        db: Session = Depends(get_database),
    ):
        logger.info(InfoDetail.func_call("conversation_history"))
        user_id = user_info["id"]
        return await self.handler.conversation_history(user_id, db)

    async def send_messsage(
        self,
        body: SendMessageRequest,
        user_info: dict = Depends(AuthService().verify_jwt_token),
        db: Session = Depends(get_database),
    ):
        logger.info(InfoDetail.func_call("send_message"))
        user_id = user_info["id"]
        return await self.handler.send_message(body, user_id, db)

    async def retrieve_conversation(
        self,
        conversation_id: int,
        db: Session = Depends(get_database),
    ):
        logger.info(InfoDetail.func_call("retrieve_conversation"))
        return await self.handler.retrieve_conversation(conversation_id, db)

    async def retrieve_itinerary(
        self,
        itinerary_id: int,
        db: Session = Depends(get_database),
    ):
        logger.info(InfoDetail.func_call("retrieve_itinerary"))
        return await self.handler.retrieve_itinerary(itinerary_id, db)

    async def retrieve_latest_itinerary(
        self,
        conversation_id: int,
        db: Session = Depends(get_database),
    ):
        logger.info(InfoDetail.func_call("retrieve_latest_itinerary"))
        return await self.handler.retrieve_latest_itinerary(conversation_id, db)
