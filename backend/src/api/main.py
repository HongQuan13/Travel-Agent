from fastapi import APIRouter

from api.ping.main import PingRouter

mainRouter = APIRouter()
ROUTE_BASE = "api/v1"
mainRouter.include_router(PingRouter().router, prefix=f"/{ROUTE_BASE}/ping")
