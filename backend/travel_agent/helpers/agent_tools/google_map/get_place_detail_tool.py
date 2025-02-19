import logging
from langchain_core.tools import StructuredTool
from pydantic import BaseModel, Field

from travel_agent.helpers.agent_tools.google_map.google_map_handler import (
    GoogleMapHandler,
)

logging.basicConfig(level=logging.INFO, force=True)
logger = logging.getLogger(__name__)


class GetPlaceDetail(BaseModel):
    place_name: str = Field(
        description="The name of the place or location that you want to search for. This can be a specific name (e.g., 'Nanyang Technological University') or a general location (e.g., 'Singapore')."
    )


get_detail_place_tool = StructuredTool.from_function(
    func=GoogleMapHandler().get_detail_place,
    name="get_detail_place_tool",
    description="""This tool retrieves detailed information about a place based on its name or location. 
    You can use it to search for places by their name (e.g., 'Nanyang Technological University') or by a general location (e.g., 'Singapore'). 
    The response will include information such as the address, opening hours, open now, phone number, reviews, and business status.""",
    args_schema=GetPlaceDetail,
)
