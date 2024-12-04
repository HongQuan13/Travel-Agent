from fastapi import APIRouter

from .subRoutes.pingRouter import PingRouter
from .subRoutes.userRouter import UserRouter
from .subRoutes.chatRouter import ChatRouter

mainRouter = APIRouter()
ROUTE_BASE = "api/v1"
mainRouter.include_router(PingRouter().router, prefix=f"/{ROUTE_BASE}/ping")
mainRouter.include_router(UserRouter().router, prefix=f"/{ROUTE_BASE}/user")
mainRouter.include_router(ChatRouter().router, prefix=f"/{ROUTE_BASE}/chat")
