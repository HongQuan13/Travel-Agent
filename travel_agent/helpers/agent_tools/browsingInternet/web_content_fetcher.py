import time
import logging
import threading
from dotenv import load_dotenv

from backend.src.constant.info_constant import InfoDetail
from travel_agent.helpers.agent_tools.browsingInternet.serper_service import (
    SerperClient,
)
from travel_agent.helpers.agent_tools.browsingInternet.web_crawler import WebCrawler


logger = logging.getLogger(__name__)


class WebContentFetcher:
    def __init__(self):
        # Initialize the fetcher with a search query
        self.web_contents = []  # Stores the fetched web contents
        self.error_urls = []  # Stores URLs that resulted in an error during fetching
        self.web_contents_lock = (
            threading.Lock()
        )  # Lock for thread-safe operations on web_contents
        self.error_urls_lock = (
            threading.Lock()
        )  # Lock for thread-safe operations on error_urls
        logger.info(f"{InfoDetail.class_initialize('WebContentFetcher')}")

    def _web_crawler_thread(self, thread_id: int, urls: list):
        # Thread function to crawl each URL
        try:
            logger.info(f"Starting web crawler thread {thread_id}")
            start_time = time.time()

            url = urls[thread_id]
            scraper = WebCrawler()
            content = scraper.scrape_url(url, 0)

            # If the scraped content is too short, try extending the crawl rules
            if 0 < len(content) < 800:
                content = scraper.scrape_url(url, 1)

            # If the content length is sufficient, add it to the shared list
            if len(content) > 300:
                with self.web_contents_lock:
                    self.web_contents.append({"url": url, "content": content})

            end_time = time.time()
            logger.info(
                f"Thread {thread_id} completed! Time consumed: {end_time - start_time:.2f}s"
            )

        except Exception as e:
            # Handle any exceptions, log the error, and store the URL
            with self.error_urls_lock:
                self.error_urls.append(url)
            logger.info(f"Thread {thread_id}: Error crawling {url}: {e}")

    def _serper_launcher(self, query: str):
        # Function to launch the Serper client and get search results
        serper_client = SerperClient()
        serper_results = serper_client.serper(query=query)
        return serper_client.extract_components(serper_results)

    def _crawl_threads_launcher(self, url_list):
        # Create and start threads for each URL in the list
        threads = []
        for i in range(len(url_list)):
            thread = threading.Thread(
                target=self._web_crawler_thread, args=(i, url_list)
            )
            threads.append(thread)
            thread.start()
        # Wait for all threads to finish execution
        for thread in threads:
            thread.join()

    def fetch(self, query: str):
        # Main method to fetch web content based on the query
        serper_response = self._serper_launcher(query=query)
        if serper_response:
            url_list = serper_response["links"]
            self._crawl_threads_launcher(url_list)
            # Reorder the fetched content to match the order of URLs
            ordered_contents = [
                next(
                    (
                        item["content"]
                        for item in self.web_contents
                        if item["url"] == url
                    ),
                    "",
                )
                for url in url_list
            ]
            return ordered_contents, serper_response
        return [], None


# Example usage
if __name__ == "__main__":
    load_dotenv()

    logging.basicConfig(level=logging.INFO, force=True)
    logger = logging.getLogger(__name__)

    fetcher = WebContentFetcher()
    contents, serper_response = fetcher.fetch("What is Asurion")

    logger.info(serper_response)
    logger.info(contents)
