import asyncio
import os
import logging
import urllib.parse
from dotenv import load_dotenv
from typing import List

from backend.src.constant.error_constant import ErrorDetail
from backend.src.constant.info_constant import InfoDetail
from travel_agent.helpers.agent_tools.image_search.s3_bucket_handler import (
    S3BucketHandler,
)
from travel_agent.helpers.api_client import APIClient

logging.basicConfig(level=logging.INFO, force=True)
logger = logging.getLogger(__name__)
load_dotenv()


class PixabaySearch:
    TOP_K = 5
    pixabay_url = "https://pixabay.com/api/"

    def __init__(self):
        self._check_env()
        self._api_client = APIClient(base_url=self.pixabay_url)
        self._s3_handler = S3BucketHandler()
        logger.info(InfoDetail.class_initialize("PixabaySearch"))

    def _check_env(self):
        pixabay_api_key = os.getenv("PIXABAY_API_KEY")

        if pixabay_api_key is None:
            raise ValueError(f"Unable to access pixabay in .env file")

        self._pixabay_api_key = pixabay_api_key

    async def _pixabay_search(self, query: str) -> List[str]:
        try:
            escaped_term = urllib.parse.quote_plus(query)
            images = []
            params = {
                "key": self._pixabay_api_key,
                "q": escaped_term,
                "image_type": "photo",
                "safesearch": "true",
            }

            data = await self._api_client.fetch(params=params)

            if "hits" in data:
                for index in range(len(data["hits"])):
                    if index >= self.TOP_K:
                        break

                    image = data["hits"][index]
                    optimized_url = self._s3_handler.image_process(
                        image["webformatURL"]
                    )
                    images.append(optimized_url)

            logger.info(f"Pixabay - Retrieve {len(images)} images for query {query}")

            return images
        except Exception as error:
            logger.error(ErrorDetail.unknown("pixabay_search", error))
            return images

    async def search_images(self, query: str):
        links = await self._pixabay_search(query)
        return links


if __name__ == "__main__":
    pixabay_search = PixabaySearch()
    asyncio.run(pixabay_search.search_images("hongkong"))
