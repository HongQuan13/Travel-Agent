import logging
import requests
import urllib.parse
from bs4 import BeautifulSoup
from typing import List

logger = logging.getLogger(__name__)


class ImageSearch:
    TOP_K = 5

    def __init__(self):
        logger.info("ImageSearch initialized")

    def _google_search(self, query: str) -> List[str]:
        try:
            escaped_term = urllib.parse.quote_plus(query)

            response = requests.get(
                url="https://www.google.com/search?tbm=isch",
                headers={"User-Agent": "Mozilla/5.0"},
                params={
                    "q": escaped_term,
                    "hl": "en",
                    "start": 0,
                    "safe": "active",
                },
                timeout=5,
            )
            response.raise_for_status()
            soup = BeautifulSoup(response.text, "html.parser")

            images = []
            for img_tag in soup.find_all("img"):
                img_url = img_tag.get("src")
                if img_url and img_url.startswith("http"):
                    images.append(img_url)

            return images

        except Exception as error:
            logger.error(f"Unknown error {error}")
            return []

    def search_images(self, query: str):
        search_results = self._google_search(query)

        links = []
        for link in search_results[: self.TOP_K]:
            links.append(link)

        output_dict = {"query": query, "links": links, "count": len(links)}

        return output_dict


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, force=True)
    logger = logging.getLogger(__name__)

    image_search = ImageSearch()
    test_query = "NTU Singapore"
    main_content = image_search.search_images(test_query)
    logger.info(main_content)
