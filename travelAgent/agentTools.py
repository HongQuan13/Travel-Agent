from langchain_community.utilities.google_serper import GoogleSerperAPIWrapper
from langchain.tools import tool
import os


@tool()
def google_search(query: str) -> str:
    """Use this tool to answer questions about current events, news, or the current state of the world where up-to-date information is required."""
    serper = GoogleSerperAPIWrapper(serper_api_key=os.getenv("SERPER_API_KEY"))
    return serper.run(query)
