import logging
from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.orm import Session

from dbs.init_postgres import getDatabase
from interfaces.user_interface import CreateUserRequest
from services.user_service import UserService

logger = logging.getLogger(__name__)


class UserRouter:
    def __init__(self):
        self.router = APIRouter()
        self.router.add_api_route("/createUser", self.create_user, methods=["POST"])
        self.handler = UserService()

    async def create_user(
        self, body: CreateUserRequest, db: Session = Depends(getDatabase)
    ):
        logger.info("create_user called")
        return await self.handler.create_user(body, db)
