import logging
from fastapi import APIRouter
from fastapi.params import Depends
from starlette.requests import Request
from sqlalchemy.orm import Session

from backend.src.constant.info_constant import InfoDetail
from backend.src.dbs.init_postgres import get_database
from backend.src.services.auth_service import AuthService

logger = logging.getLogger(__name__)


class AuthRouter:
    def __init__(self):
        self.router = APIRouter()
        self.router.add_api_route(
            "/login/google", self.login_via_google, methods=["GET"]
        )
        self.router.add_api_route("/auth/google", self.auth_via_google, methods=["GET"])
        self.router.add_api_route("/auth/verify", self.auth_verify, methods=["GET"])
        self.router.add_api_route("/auth/logout", self.logout, methods=["POST"])
        self.handler = AuthService()

    async def login_via_google(self, request: Request):
        logger.info(InfoDetail.func_call("login_via_google"))
        return await self.handler.login_via_google(request)

    async def auth_via_google(
        self, request: Request, db: Session = Depends(get_database)
    ):
        logger.info(InfoDetail.func_call("auth_via_google"))
        return await self.handler.auth_via_google(request, db)

    async def auth_verify(self, request: Request):
        logger.info(InfoDetail.func_call("auth_verify"))
        return await self.handler.verify_jwt_token(request)

    async def logout(self):
        logger.info(InfoDetail.func_call("logout"))
        return await self.handler.logout()
