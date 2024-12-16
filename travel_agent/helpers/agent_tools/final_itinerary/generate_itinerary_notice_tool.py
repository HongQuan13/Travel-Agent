import logging
from langchain_core.tools import StructuredTool

from travel_agent.helpers.agent_tools.final_itinerary.models import (
    SucessfulItineraryNotice,
)

logging.basicConfig(level=logging.INFO, force=True)
logger = logging.getLogger(__name__)


def notice_generate_itinerary_successful(itinerary_title: str):
    """Use the tool."""
    logger.info(f"notice_generate_itinerary_successful called")
    return f"Itinerary {itinerary_title} is generated successfully"


notice_generate_itinerary_successful_tool = StructuredTool.from_function(
    func=notice_generate_itinerary_successful,
    name="notice_generate_itinerary_successful_tool",
    description="""Use to notice user, deep research final itinerary generated successfully""",
    args_schema=SucessfulItineraryNotice,
)
