from langchain_community.utilities.google_serper import GoogleSerperAPIWrapper
from langchain.tools import tool
import os


@tool
def google_search(query: str) -> str:
    """
    Performs a Google search using the Serper API.

    Args:
        query (str): The search query.

    Returns:
        str: The search results as a string.
    """
    serper = GoogleSerperAPIWrapper(serper_api_key=os.getenv("SERPER_API_KEY"))
    return serper.run(query)
