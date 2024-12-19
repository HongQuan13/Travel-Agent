import logging
from fastapi import APIRouter
from fastapi.params import Depends

from backend.src.routes.sub_routes.auth_router import AuthRouter
from backend.src.routes.sub_routes.ping_router import PingRouter
from backend.src.routes.sub_routes.user_router import UserRouter
from backend.src.routes.sub_routes.chat_router import ChatRouter
from backend.src.routes.websocket.main import websocket_router
from backend.src.services.auth_service import AuthService


logger = logging.getLogger(__name__)

main_router = APIRouter()

ROUTE_BASE = "api/v1"
main_router.include_router(
    PingRouter().router,
    prefix=f"/{ROUTE_BASE}/ping",
)
main_router.include_router(AuthRouter().router, prefix=f"/{ROUTE_BASE}")
main_router.include_router(
    UserRouter().router,
    prefix=f"/{ROUTE_BASE}/user",
    dependencies=[Depends(AuthService().verify_jwt_token)],
)
main_router.include_router(
    ChatRouter().router,
    prefix=f"/{ROUTE_BASE}/chat",
    dependencies=[Depends(AuthService().verify_jwt_token)],
)
main_router.include_router(websocket_router)
