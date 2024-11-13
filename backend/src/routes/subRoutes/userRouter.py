import logging
from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.orm import Session

from dbs.initPostgres import getDatabase
from interfaces.userInterface import UserRequest
from services.userService import UserService

logger = logging.getLogger(__name__)


class UserRouter:
    def __init__(self):
        self.router = APIRouter()
        self.router.add_api_route("/createUser", self.create_user, methods=["POST"])
        self.handler = UserService()

    async def create_user(self, body: UserRequest, db: Session = Depends(getDatabase)):
        logger.info("create_user called")
        return await self.handler.create_user(body, db)
