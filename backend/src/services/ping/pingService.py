import logging

from services.ping.model import PingResponse

logger = logging.getLogger(__name__)


class PingService:
    def __init__(self):
        logger.info("PingService initialized")

    def handle_ping(self) -> str:
        return PingResponse(message="pong")
