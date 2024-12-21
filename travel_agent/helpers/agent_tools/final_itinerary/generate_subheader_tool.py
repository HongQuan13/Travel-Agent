import logging
from typing import List
from langchain_core.tools import StructuredTool

from backend.src.constant.info_constant import InfoDetail
from travel_agent.helpers.agent_tools.final_itinerary.models import Place, SubHeaders


logging.basicConfig(level=logging.INFO, force=True)
logger = logging.getLogger(__name__)


def subheaders(title: str, places: List[Place]):
    """Use the tool."""
    logger.info(InfoDetail.func_call("subheaders"))
    json_response = {
        "title": title,
        "places": places,
    }
    return json_response


generate_subheaders_tool = StructuredTool.from_function(
    func=subheaders,
    name="generate_subheaders_tool",
    description="""Use when user want to generate subheader for the final itinerary. """,
    args_schema=SubHeaders,
)
