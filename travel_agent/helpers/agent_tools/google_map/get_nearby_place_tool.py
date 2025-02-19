import logging
from typing import Literal
from langchain_core.tools import StructuredTool
from pydantic import BaseModel, Field

from travel_agent.helpers.agent_tools.google_map.google_map_handler import (
    GoogleMapHandler,
)

logging.basicConfig(level=logging.INFO, force=True)
logger = logging.getLogger(__name__)


class GetNearbyPlaces(BaseModel):
    place_name: str = Field(
        description="The name of the place or location that you want to search for. This can be a specific name (e.g., 'Nanyang Technological University') or a general location (e.g., 'Singapore')."
    )
    radius: int = Field(
        default=1000,
        description="Distance in meters within which to search for places. A larger radius will return more results but may be less relevant.",
    )
    min_price: int = Field(
        default=0,
        ge=0,
        le=4,
        description="Restricts results to places with at least this price level. Valid values are 0 (most affordable) to 4 (most expensive).",
    )
    max_price: int = Field(
        default=2,
        ge=0,
        le=4,
        description="Restricts results to places with at most this price level. Valid values are 0 (most affordable) to 4 (most expensive).",
    )
    open_now: bool = Field(
        default=False,
        description="If set to True, only returns places that are currently open for business.",
    )
    place_type: Literal[
        "amusement_park",
        "aquarium",
        "art_gallery",
        "casino",
        "museum",
        "night_club",
        "park",
        "restaurant",
        "shopping_mall",
        "tourist_attraction",
    ] = Field(
        default="tourist_attraction",
        description="The type of place to search for. Choose from common tourist categories like amusement parks, museums, or shopping malls.",
    )


get_nearby_place_tool = StructuredTool.from_function(
    func=GoogleMapHandler().get_nearby_place,
    name="get_nearby_place_tool",
    description="""Finds nearby places of interest based on a given location, radius, price range, and place type. 
    This tool helps users discover attractions, restaurants, parks, and other locations relevant to travelers.""",
    args_schema=GetNearbyPlaces,
)
