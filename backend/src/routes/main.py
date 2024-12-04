from fastapi import APIRouter

from routes.sub_routes.ping_router import PingRouter
from routes.sub_routes.user_router import UserRouter
from routes.sub_routes.chat_router import ChatRouter

main_router = APIRouter()
ROUTE_BASE = "api/v1"
main_router.include_router(PingRouter().router, prefix=f"/{ROUTE_BASE}/ping")
main_router.include_router(UserRouter().router, prefix=f"/{ROUTE_BASE}/user")
main_router.include_router(ChatRouter().router, prefix=f"/{ROUTE_BASE}/chat")
