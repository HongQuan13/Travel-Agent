import re
import logging
import requests
from bs4 import BeautifulSoup

from backend.src.constant.info_constant import InfoDetail
from travel_agent.utils.user_agents import USER_AGENTS


logger = logging.getLogger(__name__)


class WebCrawler:
    def __init__(self, user_agent="default"):
        # Initialize the scraper with a user agent (default is 'macOS')
        self.headers = USER_AGENTS[user_agent]
        logger.info(f"{InfoDetail.class_initialize('WebCrawler')}")

    def get_webpage_html(self, url):
        # Fetch the HTML content of a webpage from a given URL
        response = requests.Response()  # Create an empty Response object
        if url.endswith(".pdf"):
            # Skip PDF files which are time consuming
            return response

        try:
            # Attempt to get the webpage content with specified headers and timeout
            response = requests.get(url, headers=self.headers, timeout=8)
            response.encoding = "utf-8"
        except requests.exceptions.Timeout:
            # Add timeout exception handling here
            return response

        return response

    def convert_html_to_soup(self, html):
        # Convert the HTML string to a BeautifulSoup object for parsing
        html_string = html.text
        return BeautifulSoup(html_string, "lxml")

    def extract_main_content(self, html_soup, rule=0):
        # Extract the main content from a BeautifulSoup object
        main_content = []
        find_tag_elements = ["h[1-6]", "p", "li"]
        if rule == 1:
            find_tag_elements.append("div")
        tag_rule = re.compile(f"^({('|').join(find_tag_elements)})")
        # Iterate through specified tags and collect their text
        for tag in html_soup.find_all(tag_rule):
            tag_text = tag.get_text().strip()
            if tag_text:
                main_content.append(tag_text)
        return "\n".join(main_content).strip()

    def scrape_url(self, url, rule=0):
        # Public method to scrape a URL and extract its main content
        webpage_html = self.get_webpage_html(url)
        soup = self.convert_html_to_soup(webpage_html)
        main_content = self.extract_main_content(soup, rule)
        return main_content


# Example usage
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, force=True)
    logger = logging.getLogger(__name__)

    scraper = WebCrawler(user_agent="macOS")
    test_url = "https://www.asurion.com/about"
    main_content = scraper.scrape_url(test_url)
    logger.info(main_content)
