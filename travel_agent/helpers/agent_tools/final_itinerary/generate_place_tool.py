import logging
from langchain_core.tools import StructuredTool

from travel_agent.helpers.agent_tools.final_itinerary.models import Place

logging.basicConfig(level=logging.INFO, force=True)
logger = logging.getLogger(__name__)


def generate_place(placeName: str, address: str, description: str):
    """Use the tool."""
    logger.info(f"place_detail called")
    json_response = {
        "placeName": placeName,
        "address": address,
        "description": description,
    }
    return json_response


generate_place_tool = StructuredTool.from_function(
    func=generate_place,
    name="place_detail_tool",
    description="""Use when user want to generate each place detail. """,
    args_schema=Place,
)
