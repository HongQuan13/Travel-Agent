import logging
from typing import Literal
from langchain_core.tools import StructuredTool
from pydantic import BaseModel, Field

from travel_agent.helpers.agent_tools.google_map.google_map_handler import (
    GoogleMapHandler,
)

logging.basicConfig(level=logging.INFO, force=True)
logger = logging.getLogger(__name__)


class GetDistance(BaseModel):
    origin: str = Field(
        description="The starting location from where the journey begins. It can be a full address, place name, or coordinates."
    )
    destination: str = Field(
        description="The ending location where the journey will conclude. Similar to the origin, it can be an address, place name, or coordinates."
    )
    mode: Literal["driving", "walking", "transit", "bicycling"] = Field(
        default="driving",
        description="The mode of transportation for calculating the travel distance and duration. Choose from: 'driving', 'walking', 'transit', or 'bicycling'.",
    )


get_distance_tool = StructuredTool.from_function(
    name="get_distance_tool",
    func=GoogleMapHandler().get_distance,
    description="""This tool is used to retrieve the travel distance and estimated travel duration between two locations. 
    It allows you to choose the mode of transportation: driving, walking, transit, or bicycling. """,
    args_schema=GetDistance,
)
