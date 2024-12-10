import logging
from fastapi import APIRouter

from backend.src.lib.websocket import WebSocketManager
from backend.src.routes.sub_routes.ping_router import PingRouter
from backend.src.routes.sub_routes.user_router import UserRouter
from backend.src.routes.sub_routes.chat_router import ChatRouter
from backend.src.routes.websocket.main import WebSocketRouter


logger = logging.getLogger(__name__)

main_router = APIRouter()
manager = WebSocketManager()

ROUTE_BASE = "api/v1"
main_router.include_router(PingRouter().router, prefix=f"/{ROUTE_BASE}/ping")
main_router.include_router(UserRouter().router, prefix=f"/{ROUTE_BASE}/user")
main_router.include_router(ChatRouter().router, prefix=f"/{ROUTE_BASE}/chat")
main_router.include_router(WebSocketRouter().router)
