from pydantic import BaseModel
from langchain_core.tools import StructuredTool

from travel_agent.helpers.agent_tools.image_search.tavily_search import TavilySearch


class ImageSearchInput(BaseModel):
    query: str


def image_search(query: str) -> str:
    search_agent = TavilySearch()
    return search_agent.search_images(query)


image_search_tool = StructuredTool.from_function(
    func=image_search,
    name="image_search_tool",
    description="Use this tool to retrieve images related to a place or anything else relevant to travel planning.",
    args_schema=ImageSearchInput,
)
