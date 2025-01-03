import os
from langchain.tools import tool
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_community.utilities.google_serper import GoogleSerperAPIWrapper


@tool()
def google_search(query: str) -> str:
    """Use when searching information about a place or event. Do not use it for image search"""
    serper = GoogleSerperAPIWrapper(serper_api_key=os.getenv("SERPER_API_KEY"))
    return serper.run(query)


@tool()
def duckduckgo_search(query: str) -> str:
    """Use when searching information about a place or event. Do not use it for image search"""
    search = DuckDuckGoSearchRun()
    return search.run(query)
