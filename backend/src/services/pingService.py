import logging

from interfaces.pingInterface import PingResponse

logger = logging.getLogger(__name__)


class PingService:
    def __init__(self):
        logger.info("PingService initialized")

    def handle_ping(self):
        return PingResponse(message="pong")
