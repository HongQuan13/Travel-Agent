import logging
import requests
import urllib.parse
from bs4 import BeautifulSoup
from typing import List, Optional

from backend.src.constant.error_constant import ErrorDetail
from backend.src.constant.info_constant import InfoDetail
from travel_agent.utils.user_agents import USER_AGENTS


logger = logging.getLogger(__name__)


class SerperClient:
    TOP_K = 3

    def __init__(
        self, user_agent="default", whitelisted_sites: Optional[List[str]] = None
    ):
        self.whitelisted_sites = whitelisted_sites
        self.headers = USER_AGENTS[user_agent]

        logger.info(f"{InfoDetail.class_initialize('SerperClient')}")

    def serper(self, query: str):
        search_links = []
        crawl_functions = [self._google_search, self._bing_search]
        while len(search_links) == 0 and len(crawl_functions) != 0:
            search_links.extend(crawl_functions[-1](query))
            crawl_functions.pop()
        search_reponses = {"links": search_links, "query": query}
        return search_reponses

    def _bing_search(self, query: str) -> List[str]:
        try:
            escaped_term = urllib.parse.quote_plus(query)
            response = requests.get(
                url="https://www.bing.com/search",
                headers=self.headers,
                params={
                    "q": escaped_term,
                },
                timeout=5,
            )
            # Parse
            soup = BeautifulSoup(response.text, "html.parser")
            result_block = soup.find_all("li", attrs={"class": "b_algo"})

            search_links = []
            for result in result_block:
                # Find link, title, description
                link = result.find("a", href=True)
                title = result.find("h2")
                description_box = result.find("p")
                if description_box:
                    description = description_box.text
                    if link and title and description:
                        search_links.append(link["href"])
            return search_links
        except Exception as error:
            logger.error(f"{ErrorDetail.unknown('_bing_search',error)}")
            return []

    def _google_search(self, query: str) -> List[str]:
        try:
            escaped_term = urllib.parse.quote_plus(query)

            response = requests.get(
                url="https://www.google.com/search",
                headers=self.headers,
                params={
                    "q": escaped_term,
                    "hl": "en",
                    "start": 0,
                    "safe": "active",
                },
                timeout=5,
            )
            # Parse
            soup = BeautifulSoup(response.text, "html.parser")
            result_block = soup.find_all("div", attrs={"class": "g"})

            search_links = []
            for result in result_block:
                # Find link, title, description
                link = result.find("a", href=True)
                title = result.find("h3")
                description_box = result.find("div", {"style": "-webkit-line-clamp:2"})
                if description_box:
                    description = description_box.text
                    if link and title and description:
                        search_links.append(link["href"])
            return search_links
        except Exception as error:
            logger.error(f"{ErrorDetail.unknown('_google_search',error)}")
            return []

    def extract_components(self, serper_response: dict):
        # Initialize lists to store the extracted components
        links = []

        # Iterate through the 'organic' section of the response and extract information
        for link in serper_response.get("links", []):
            links.append(link)
            if len(links) >= self.TOP_K:
                break

        # Retrieve additional information from the response
        query = serper_response.get("query", "")
        # Organize the extracted data into a dictionary and return
        output_dict = {"query": query, "links": links, "count": len(links)}

        return output_dict
