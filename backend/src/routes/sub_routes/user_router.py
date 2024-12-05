import logging
from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.orm import Session

from backend.src.dbs.init_postgres import get_database
from backend.src.interfaces.user_interface import CreateUserRequest
from backend.src.services.user_service import UserService

logger = logging.getLogger(__name__)


class UserRouter:
    def __init__(self):
        self.router = APIRouter()
        self.router.add_api_route("/create-user", self.create_user, methods=["POST"])
        self.handler = UserService()

    async def create_user(
        self, body: CreateUserRequest, db: Session = Depends(get_database)
    ):
        logger.info("create_user called")
        return await self.handler.create_user(body, db)
