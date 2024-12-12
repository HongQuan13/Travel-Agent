from pydantic import BaseModel
from langchain_core.tools import StructuredTool

from travel_agent.helpers.agent_tools.image_search.browser_internet import ImageSearch


class ImageSearchInput(BaseModel):
    query: str


def image_search(query: str) -> str:
    search_agent = ImageSearch()
    return search_agent.search_images(query)


image_search_tool = StructuredTool.from_function(
    func=image_search,
    name="image_search_tool",
    description="Use this tool to retrieve images related to a place or anything else relevant to travel planning.",
    args_schema=ImageSearchInput,
)
