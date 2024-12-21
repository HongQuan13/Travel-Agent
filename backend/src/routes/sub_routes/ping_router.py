import logging
from fastapi import APIRouter

from backend.src.constant.info_constant import InfoDetail
from backend.src.services.ping_service import PingService

logger = logging.getLogger(__name__)


class PingRouter:
    def __init__(self):
        self.router = APIRouter()
        self.router.add_api_route("", self.call_ping, methods=["GET"])
        self.handler = PingService()

    def call_ping(self):
        logger.info(InfoDetail.func_call("call_ping"))
        return self.handler.handle_ping()
