import asyncio
import json
import logging
from typing import Dict, List
from langchain_core.tools import StructuredTool
from pydantic import BaseModel, Field, validator

from backend.src.dbs.init_postgres import get_database
from backend.src.lib.websocket import WebSocketManager
from backend.src.models.plan_model import Plan

logging.basicConfig(level=logging.INFO, force=True)
logger = logging.getLogger(__name__)


class ImageUrl(BaseModel):
    image_url: str = Field(description="Image url associated with the place or event")


class Place(BaseModel):
    placeName: str = Field(description="The name of the place or event")
    address: str = Field(description="The geographical address of the place or event.")
    description: str = Field(description="A brief summary of the place or event.")


class DeepResearchInput(BaseModel):
    mainHeader: str = Field(
        description="The primary title or header for the generated plan, summarizing its main focus or theme."
    )
    images: List[ImageUrl] = Field(
        description="List of images about places or event inside plan",
    )
    subHeaders: Dict[str, List[Place]] = Field(
        description="""A dictionary where each key is a subheader (a brief descriptive title), 
        and each value is a list of Place objects associated with that subheader.""",
    )

    @validator("images")
    def validate_images_not_empty(cls, value):
        if not value:
            raise ValueError("The 'images' list must contain at least one item.")
        return value


def save_final_plan(plan_detail: str):
    db = get_database()
    session = next(db)
    new_plan = Plan(plan_detail=plan_detail)
    session.add(new_plan)
    session.commit()
    logger.info(f"Create new plan {new_plan.id} successfully")


def deep_research_plan(
    mainHeader: str,
    subHeaders: Dict[str, List[Place]],
) -> object:
    """Use the tool."""
    logger.info(f"deep_research_plan called")
    json_response = {
        "mainHead": mainHeader,
        "subHeaders": subHeaders,
    }
    jsong_dumps = json.dumps(
        json_response, default=lambda o: o.dict() if hasattr(o, "dict") else o
    )

    save_final_plan(jsong_dumps)
    asyncio.run(WebSocketManager().broadcast(jsong_dumps))
    return


deep_research_plan_tool = StructuredTool.from_function(
    func=deep_research_plan,
    name="deep_research_plan_tool",
    description="""
        Use when user want to generate a deep research for visualization purposes. 
        It formats travel-related data, such as itineraries, restaurant lists, or place details, into a finalized structure.

        Output is not returned to the user but confirms the successful generation of the final plan.

        Example Input:
        {
            "mainHeader": "Seattle Instagram Getaway", 
            "images": ["https://res.cloudinary.com/ducz9g7pb/image/upload/c_auto,f_auto,g_auto,h_270,q_auto,w_480/v1/travel-agent/v2dtdyvuddly2u2ehfzz"]
            "subHeaders": {
                "Day-1": [
                    {
                        "placeName": "Nanyang Technological University",
                        "address": "50 Nanyang Ave, Singapore 639798",
                        "description": "A top-ranked global university excelling in research, innovation, and education."
                    }
                ]
            }
        }
    """,
    args_schema=DeepResearchInput,
)
