import logging
from fastapi import APIRouter
from starlette.requests import Request

from backend.src.services.auth_service import AuthService

logger = logging.getLogger(__name__)


class AuthRouter:
    def __init__(self):
        self.router = APIRouter()
        self.router.add_api_route(
            "/login/google", self.login_via_google, methods=["GET"]
        )
        self.router.add_api_route("/auth/google", self.auth_via_google, methods=["GET"])
        self.handler = AuthService()

    async def login_via_google(self, request: Request):
        logger.info("login_via_google called")
        return await self.handler.login_via_google(request)

    async def auth_via_google(self, request: Request):
        logger.info("auth_via_google called")
        return await self.handler.auth_via_google(request)
