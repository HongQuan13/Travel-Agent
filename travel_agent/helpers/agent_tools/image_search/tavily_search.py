import logging
import urllib.parse
from tavily import TavilyClient
from typing import List

logger = logging.getLogger(__name__)


class TavilySearch:
    TOP_K = 5

    def __init__(self):
        self._tavily_client = TavilyClient()
        logger.info("ImageSearch initialized")

    def _tavily_search(self, query: str) -> List[str]:
        try:
            escaped_term = urllib.parse.quote_plus(query)
            response = self._tavily_client.search(
                escaped_term, include_images=True, max_results=self.TOP_K
            )

            images = []
            for image in response["images"]:
                images.append(image)

            return images

        except Exception as error:
            logger.error(f"Unknown error {error}")
            return []

    def search_images(self, query: str):
        links = self._tavily_search(query)

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
