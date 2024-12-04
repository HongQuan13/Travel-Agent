from fastapi import APIRouter

from routes.sub_routes.ping_router import PingRouter
from routes.sub_routes.user_router import UserRouter
from routes.sub_routes.chat_router import ChatRouter

mainRouter = APIRouter()
ROUTE_BASE = "api/v1"
mainRouter.include_router(PingRouter().router, prefix=f"/{ROUTE_BASE}/ping")
mainRouter.include_router(UserRouter().router, prefix=f"/{ROUTE_BASE}/user")
mainRouter.include_router(ChatRouter().router, prefix=f"/{ROUTE_BASE}/chat")
