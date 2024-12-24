import logging
from langchain_core.tools import StructuredTool
from pydantic import BaseModel, Field

from travel_agent.helpers.agent_tools.google_map.google_map_handler import (
    GoogleMapHandler,
)

logging.basicConfig(level=logging.INFO, force=True)
logger = logging.getLogger(__name__)


class GetGeocode(BaseModel):
    place_name: str = Field(description="Place name or location of searching place")


generate_place_tool = StructuredTool.from_function(
    func=GoogleMapHandler().get_geocode,
    name="generate_place_tool",
    description="""Use to retrieve the location and geographic coordinates including longtitude and latitude """,
    args_schema=GetGeocode,
)
