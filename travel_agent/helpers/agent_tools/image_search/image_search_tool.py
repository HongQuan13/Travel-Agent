import asyncio
from pydantic import BaseModel
from langchain_core.tools import StructuredTool

from travel_agent.helpers.agent_tools.image_search.tavily_search import TavilySearch


class ImageSearchInput(BaseModel):
    query: str


def image_search(query: str) -> str:
    search_agent = TavilySearch()
    result = asyncio.run(search_agent.search_images(query))
    return result


image_search_tool = StructuredTool.from_function(
    func=image_search,
    name="image_search_tool",
    description="Retrieves a list of images related to a specific place",
    args_schema=ImageSearchInput,
)
