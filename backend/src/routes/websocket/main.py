import logging
from fastapi import APIRouter, WebSocket, WebSocketDisconnect

from backend.src.lib.websocket import WebSocketManager

logger = logging.getLogger(__name__)

manager = WebSocketManager()
websocket_router = APIRouter()


@websocket_router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            logger.info(f"Received: {data}")
            await manager.broadcast("hello back")
    except WebSocketDisconnect:
        manager.disconnect(websocket)


@websocket_router.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: int):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            logger.info(f"Received from {client_id}: {data}")
            await manager.broadcast(f"Client #{client_id} says: {data}")
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        logger.info(f"Client #{client_id} left the chat")
        await manager.broadcast(f"Client #{client_id} left the chat")


# class WebSocketRouter:
#     def __init__(self):
#         self.manager = WebSocketManager()
#         self.router = APIRouter()
#         self.router.add_websocket_route("/ws", self.websocket_endpoint)
#         self.router.add_websocket_route(
#             "/ws/{client_id}", self.websocket_with_client_id
#         )

#     async def websocket_endpoint(self,websocket: WebSocket):
#         await manager.connect(websocket)
#         try:
#             while True:
#                 data = await websocket.receive_text()
#         except WebSocketDisconnect:
#             manager.disconnect(websocket)

#     async def websocket_with_client_id(websocket: WebSocket, client_id: int):
#         await manager.connect(websocket)
#         try:
#             while True:
#                 data = await websocket.receive_text()
#                 logger.info(f"Received from {client_id}: {data}")
#                 await manager.broadcast(f"Client #{client_id} says: {data}")
#         except WebSocketDisconnect:
#             manager.disconnect(websocket)
#             logger.info(f"Client #{client_id} left the chat")
#             await manager.broadcast(f"Client #{client_id} left the chat")
