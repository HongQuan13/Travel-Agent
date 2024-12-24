import logging
from datetime import datetime
from langchain_core.tools import StructuredTool
from pydantic import BaseModel, Field

from backend.src.constant.info_constant import InfoDetail
from travel_agent.helpers.agent_tools.browsingInternet.helpers import format_docs
from travel_agent.helpers.agent_tools.browsingInternet.in_memory_chroma import (
    InMemeoryChroma,
)
from travel_agent.helpers.agent_tools.browsingInternet.web_content_fetcher import (
    WebContentFetcher,
)

logging.basicConfig(level=logging.INFO, force=True)
logger = logging.getLogger(__name__)


class InternetBrowser(BaseModel):
    query: str = Field(description="The place name or search keyword")


def browser_internet(query: str) -> str:
    logger.info(f"{InfoDetail.class_initialize('browser_internet')}")
    in_memory_retriever = InMemeoryChroma(
        is_persistent=False,
        collection_name=f"InMemoryChroma_{datetime.now().timestamp()}",
    )

    web_contents_fetcher = WebContentFetcher()
    web_contents, serper_response = web_contents_fetcher.fetch(query)

    if serper_response["count"] == 0:
        return "There is no content from the trusted websites. Consider using another tool."

    metadatas = [{"url": link} for link in serper_response["links"]]
    in_memory_retriever.add_embeddings(texts=web_contents, metadatas=metadatas)

    documents = in_memory_retriever.retrieve_embeddings(query)
    relevant_docs_text, links = format_docs(documents)

    return relevant_docs_text


browser_internet_tool = StructuredTool.from_function(
    func=browser_internet,
    name="browser_internet_tool",
    description=""" Use when searching information about a place, event or related to travel plan. Do not use it for image search  """,
    args_schema=InternetBrowser,
)
