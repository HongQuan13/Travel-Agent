import json
import logging
from typing import Dict, List, Optional, Type
from langchain_core.callbacks import (
    CallbackManagerForToolRun,
    AsyncCallbackManagerForToolRun,
)
from langchain_core.tools import BaseTool, StructuredTool
from pydantic import BaseModel, Field

logging.basicConfig(level=logging.INFO, force=True)
logger = logging.getLogger(__name__)


class ImageUrl(BaseModel):
    image_url: str = Field(
        description="URLs or paths to images associated with the place or activity."
    )


class Place(BaseModel):
    placeName: str = Field(description="The name of the location or activity.")
    location: str = Field(
        description="The geographical location of the activity or event."
    )
    description: str = Field(description="A brief summary of the place or activity.")
    images: Optional[List[ImageUrl]] = Field(
        default=None, description="Optional images for the place or activity."
    )


class FinalizePlanInput(BaseModel):
    isFinalized: bool = Field(
        ..., description="Indicates whether the plan has been finalized."
    )
    mainHeader: str = Field(description="The main header or title for the travel plan.")
    subHeaders: Dict[str, List[Place]] = Field(
        description="A dictionary containing subheaders as keys and lists of places as values.",
    )


def finalize_plan(
    isFinalized: bool,
    mainHeader: str,
    subHeaders: Dict[str, List[Place]],
) -> object:
    """Use the tool."""
    logger.info(f"finalize_plan called")
    json_response = {
        "isFinalized": isFinalized,
        "mainHead": mainHeader,
        "subHeaders": subHeaders,
    }
    return json_response


finalize_plan_tool = StructuredTool.from_function(
    func=finalize_plan,
    name="finalize_plan_tool",
    description="""
    This function is used to format the finalized version of the data for travel-related queries, such as travel plans, lists of restaurants, or details about places.
    The output is designed to be versatile and suitable for frontend or backend applications.

    Use Cases:
    - Finalizing a travel plan with detailed itinerary.
    - Providing a structured list of restaurants or attractions.
    - Summarizing details about specific places or activities.

    Only return the json format output without any explaination:
    Example output:
    {
    "isFinalized": true,
    "mainHeader": "Seattle Instagram Getaway",
    "subHeaders": {
        "Day-1": [
            {
                "placeName": "Pike Place Market",
                "location": "Seattle, WA",
                "description": "A historic market overlooking the waterfront, featuring local vendors and unique goods.",
                "images": []
            }
            ],
        }
    }
    """,
    args_schema=FinalizePlanInput,
)
