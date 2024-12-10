import json
import logging
from typing import Dict, List, Optional
from langchain_core.tools import StructuredTool, ToolException
from pydantic import BaseModel, Field

from backend.src.dbs.init_postgres import get_database
from backend.src.models.plan_model import Plan

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


def save_final_plan(plan_detail: str):
    db = get_database()
    session = next(db)
    new_plan = Plan(plan_detail=plan_detail)
    session.add(new_plan)
    session.commit()
    logger.info(f"Create new plan {new_plan.id} successfully")


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
    jsong_dumps = json.dumps(
        json_response, default=lambda o: o.dict() if hasattr(o, "dict") else o
    )

    save_final_plan(jsong_dumps)
    return "/internal"


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

    Whenever finalize_plan_tool run successfully, only return "/internal".
    Example input:
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
    # return_direct=True,
)
