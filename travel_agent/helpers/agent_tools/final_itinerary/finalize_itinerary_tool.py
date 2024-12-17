import asyncio
import json
import logging
from typing import List
from fastapi.encoders import jsonable_encoder
from langchain_core.tools import StructuredTool

from backend.src.lib.websocket import WebSocketManager
from travel_agent.helpers.agent_tools.final_itinerary.helper import (
    save_final_itinerary,
    save_itinerary_message,
)
from travel_agent.helpers.agent_tools.final_itinerary.models import (
    FinalItinerary,
    ImageUrl,
    SubHeaders,
)

logging.basicConfig(level=logging.INFO, force=True)
logger = logging.getLogger(__name__)


def finalize_itinerary(
    mainHeader: str,
    images: List[ImageUrl],
    subHeaders: List[SubHeaders],
) -> object:
    """Use the tool."""
    logger.info(f"finalize_itinerary called")
    json_response = {
        "mainHeader": mainHeader,
        "images": images,
        "subHeaders": subHeaders,
    }
    jsong_dumps = json.dumps(jsonable_encoder(json_response))

    plan_id = save_final_itinerary(jsong_dumps)
    save_itinerary_message(plan_id)

    # hardcode conversation_id = 1
    socket_message = {
        "conversation_id": 1,
        "plan_id": plan_id,
        "plan_detail": jsonable_encoder(json_response),
    }
    asyncio.run(WebSocketManager().broadcast(json.dumps(socket_message)))
    return


finalize_itinerary_tool = StructuredTool.from_function(
    func=finalize_itinerary,
    name="finalize_itinerary_tool",
    description="""
        Use when user want to generate the final itinerary. 
        It formats travel-related data, such as itineraries, restaurant lists, or place details, into a finalized structure.

        Output is not returned to the user but confirms the successful generation of the final itinerary.

        Example Input:
        {
            "mainHeader": "Seattle Instagram Getaway", 
            "images": [{"image_url": "https://example.com/image.jpg"}],
            "subHeaders": [
                {
                "title": "Day-1",
                "places": [
                    {
                        "placeName": "Nanyang Technological University",
                        "address": "50 Nanyang Ave, Singapore 639798",
                        "description": "A top-ranked global university excelling in research, innovation, and education."
                    },
                    ]
                },
            ]
        }
    """,
    args_schema=FinalItinerary,
)
