import asyncio
import json
import logging
from typing import List
from fastapi.encoders import jsonable_encoder
from langchain_core.tools import StructuredTool
from pydantic import BaseModel, Field, validator

from backend.src.dbs.init_postgres import get_database
from backend.src.lib.websocket import WebSocketManager
from backend.src.models.plan_model import Plan

logging.basicConfig(level=logging.INFO, force=True)
logger = logging.getLogger(__name__)


class ImageUrl(BaseModel):
    image_url: str = Field(description="Image url associated with the place or event")

    @validator("image_url")
    def validate_url(cls, value):
        if not value.startswith(("http://", "https://")):
            raise ValueError(
                "The 'image_url' must be a valid URL starting with 'http://' or 'https://'."
            )
        return value


class Place(BaseModel):
    placeName: str = Field(description="The name of the place or event")
    address: str = Field(description="The geographical address of the place or event.")
    description: str = Field(description="A brief summary of the place or event.")


class SubHeaders(BaseModel):
    title: str = Field(description="A short descritive title")
    places: List[Place] = Field(
        description="A list of Place objects associated with that subheader."
    )


class DeepResearchInput(BaseModel):
    mainHeader: str = Field(
        description="The primary title or header for the generated plan, summarizing its main focus or theme."
    )
    images: List[ImageUrl] = Field(
        description="List of images about places or event inside plan",
    )
    subHeaders: List[SubHeaders] = Field(
        description="""List of subheaders inside plan""",
    )

    @validator("images")
    def validate_images_content(cls, value):
        if not isinstance(value, ImageUrl):
            raise ValueError("Each item in 'images' must be an ImageUrl object.")
        return value


def save_final_plan(plan_detail: str):
    db = get_database()
    session = next(db)
    new_plan = Plan(plan_detail=plan_detail)

    try:
        session.add(new_plan)
        session.commit()
        logger.info(f"Create new plan {new_plan.id} successfully")
    except Exception as e:
        session.rollback()
        logger.error(f"Error saving plan: {e}")
        raise


def place_detail(placeName: str, address: str, description: str):
    """Use the tool."""
    logger.info(f"place_detail called")
    json_response = {
        "placeName": placeName,
        "address": address,
        "description": description,
    }
    return json_response


def subheaders(title: str, places: List[Place]):
    """Use the tool."""
    logger.info(f"subheaders called")
    json_response = {
        "title": title,
        "places": places,
    }
    return json_response


def deep_research_plan(
    mainHeader: str,
    images: List[ImageUrl],
    subHeaders: List[SubHeaders],
) -> object:
    """Use the tool."""
    logger.info(f"deep_research_plan called")
    json_response = {
        "mainHeader": mainHeader,
        "images": images,
        "subHeaders": subHeaders,
    }
    jsong_dumps = json.dumps(jsonable_encoder(json_response))

    save_final_plan(jsong_dumps)
    asyncio.run(WebSocketManager().broadcast(jsong_dumps))
    return


place_detail_tool = StructuredTool.from_function(
    func=place_detail,
    name="place_detail_tool",
    description="""Use when user want to generate each place detail. """,
    args_schema=Place,
)

subheaders_tool = StructuredTool.from_function(
    func=subheaders,
    name="subheaders_tool",
    description="""Use when user want to generate subheader for the deep_research_plan. """,
    args_schema=SubHeaders,
)

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
    args_schema=DeepResearchInput,
)
