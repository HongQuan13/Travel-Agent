import logging
from typing import List
from langchain_core.tools import StructuredTool

from backend.src.constant.info_constant import InfoDetail
from travel_agent.helpers.agent_tools.final_itinerary.models import Place, Review

logging.basicConfig(level=logging.INFO, force=True)
logger = logging.getLogger(__name__)


def generate_place(
    placeName: str,
    address: str,
    description: str,
    current_opening_hours: str,
    geometry: str,
    reviews: List[Review],
    international_phone_number: str = "",
):
    """Use the tool."""
    logger.info(InfoDetail.func_call("generate_place"))
    json_response = {
        "placeName": placeName,
        "address": address,
        "description": description,
        "current_opening_hours": current_opening_hours,
        "geometry": geometry,
        "international_phone_number": international_phone_number,
        "reviews": reviews,
    }
    return json_response


generate_place_tool = StructuredTool.from_function(
    func=generate_place,
    name="place_detail_tool",
    description="""Use when user want to generate each place detail. """,
    args_schema=Place,
)
