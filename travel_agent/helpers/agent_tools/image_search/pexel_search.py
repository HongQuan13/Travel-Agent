import os
import logging
import requests
import urllib.parse
from dotenv import load_dotenv
from typing import List

from backend.src.constant.error_constant import ErrorDetail
from backend.src.constant.info_constant import InfoDetail
from travel_agent.helpers.agent_tools.image_search.s3_bucket_handler import (
    S3BucketHandler,
)

logging.basicConfig(level=logging.INFO, force=True)
logger = logging.getLogger(__name__)
load_dotenv()


class PexelSearch:
    TOP_K = 5
    pexel_url = "https://api.pexels.com/v1/search"

    def __init__(self):
        self._check_env()
        self._s3_handler = S3BucketHandler()
        logger.info(InfoDetail.class_initialize("PexelSearch"))

    def _check_env(self):
        pexel_api_key = os.getenv("PEXEL_API_KEY")

        if pexel_api_key is None:
            raise ValueError(f"Unable to access pexel in .env file")

        self._pexel_api_key = pexel_api_key

    def _pexel_search(self, query: str) -> List[str]:
        try:
            escaped_term = urllib.parse.quote_plus(query)
            images = []
            headers = {"Authorization": self._pexel_api_key}
            params = {
                "query": escaped_term,
                "size": "medium",
            }

            response = requests.get(self.pexel_url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()

            if "photos" in data:
                for index in range(len(data["photos"])):
                    if index >= self.TOP_K:
                        break

                    image = data["photos"][index]
                    optimized_url = self._s3_handler.image_process(
                        image["src"]["medium"]
                    )
                    images.append(optimized_url)

            logger.info(f"Pexel - Retrieve {len(images)} images for query {query}")

            return images
        except Exception as error:
            logger.error(ErrorDetail.unknown("pexel_search", error))
            return images

    def search_images(self, query: str):
        links = self._pexel_search(query)
        return links


if __name__ == "__main__":
    pexel_search = PexelSearch()
    pexel_search.search_images("hongkong")
