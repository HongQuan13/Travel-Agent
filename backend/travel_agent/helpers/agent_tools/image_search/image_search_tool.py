import asyncio
from pydantic import BaseModel
from langchain_core.tools import StructuredTool

from travel_agent.helpers.agent_tools.image_search.pexel_search import PexelSearch
from travel_agent.helpers.agent_tools.image_search.pixabay_search import PixabaySearch
from travel_agent.helpers.agent_tools.image_search.tavily_search import TavilySearch


class ImageSearchInput(BaseModel):
    query: str


def image_search(query: str, top_k: int = 5) -> str:
    result = []
    agents = [PixabaySearch(), PexelSearch(), TavilySearch()]

    for agent in agents:
        agent_results = asyncio.run(agent.search_images(query))
        result.extend(agent_results)

        if len(result) >= top_k:
            break

    output_dict = {
        "query": query,
        "links": result,
        "count": len(result),
    }

    return output_dict


image_search_tool = StructuredTool.from_function(
    func=image_search,
    name="image_search_tool",
    description="Retrieves a list of images related to a specific place",
    args_schema=ImageSearchInput,
)
