import logging

from src.constant.info_constant import InfoDetail
from src.interfaces.ping_interface import PingResponse

logger = logging.getLogger(__name__)


class PingService:
    def __init__(self):
        logger.info(InfoDetail.class_initialize("PingService"))

    def handle_ping(self):
        return PingResponse(message="pong")
