import logging
from fastapi import APIRouter, WebSocket, WebSocketDisconnect

from backend.src.lib.websocket import WebSocketManager

logger = logging.getLogger(__name__)


class WebSocketRouter:
    def __init__(self):
        self.manager = WebSocketManager()
        self.router = APIRouter()
        self.router.add_websocket_route("/ws", self.websocket_endpoint)
        self.router.add_websocket_route(
            "/ws/{client_id}", self.websocket_with_client_id
        )

    async def websocket_endpoint(self, websocket: WebSocket):
        """WebSocket endpoint for general connections."""
        await self.manager.connect(websocket)
        try:
            while True:
                data = await websocket.receive_text()
                logger.info(f"Received: {data}")
        except WebSocketDisconnect:
            self.manager.disconnect(websocket)

    async def websocket_with_client_id(self, websocket: WebSocket, client_id: int):
        """WebSocket endpoint for client-specific connections."""
        await self.manager.connect(websocket, client_id=client_id)
        try:
            while True:
                data = await websocket.receive_text()
                logger.info(f"Received from client {client_id}: {data}")
                await self.manager.broadcast(f"Client {client_id} says: {data}")
        except WebSocketDisconnect:
            self.manager.disconnect(websocket)
            logger.info(f"Client {client_id} disconnected")
            await self.manager.broadcast(f"Client {client_id} left the chat")
