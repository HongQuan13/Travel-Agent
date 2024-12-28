import os
import logging
import urllib.parse
from dotenv import load_dotenv
from tavily import TavilyClient
from typing import List

from backend.src.constant.error_constant import ErrorDetail
from backend.src.constant.info_constant import InfoDetail
from travel_agent.helpers.agent_tools.image_search.s3_bucket_handler import (
    S3BucketHandler,
)

logging.basicConfig(level=logging.INFO, force=True)
logger = logging.getLogger(__name__)
load_dotenv()


class TavilySearch:
    TOP_K = 5

    def __init__(self):
        self._check_env()
        self._tavily_client = TavilyClient()
        self._s3_handler = S3BucketHandler()
        logger.info(InfoDetail.class_initialize("ImageSearch"))

    def _check_env(self):
        tavily_api_key = os.getenv("TAVILY_API_KEY")

        if tavily_api_key is None:
            raise ValueError(f"Unable to access TAVILY_API_KEY in .env file")

    async def _tavily_search(self, query: str) -> List[str]:
        try:
            escaped_term = urllib.parse.quote_plus(query)
            response = self._tavily_client.search(
                escaped_term, include_images=True, max_results=self.TOP_K
            )

            images = []
            for image in response["images"]:
                optimized_url = self._s3_handler.image_process(image)
                images.append(optimized_url)

            return images

        except Exception as error:
            logger.error(ErrorDetail.unknown("tavily_search", error))
            return images

    async def search_images(self, query: str):
        links = await self._tavily_search(query)

        if len(links) == 0:
            output_dict = {
                "query": query,
                "links": "https://res.cloudinary.com/ducz9g7pb/image/upload/c_auto,f_auto,g_auto,h_270,q_auto,w_480/v1/travel-agent/v2dtdyvuddly2u2ehfzz",
                "count": 1,
            }
        else:
            output_dict = {
                "query": query,
                "links": links,
                "count": len(links),
            }

        return output_dict


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, force=True)
    logger = logging.getLogger(__name__)

    image_search = TavilySearch()
    test_query = "NTU Singapore"
    main_content = image_search.search_images(test_query)
    logger.info(main_content)
