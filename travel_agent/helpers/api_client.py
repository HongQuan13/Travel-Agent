import asyncio
import json
import logging
import httpx
from asyncio_throttle import Throttler
from tenacity import retry, stop_after_attempt, wait_exponential

from backend.src.constant.error_constant import ErrorDetail

logging.basicConfig(level=logging.INFO, force=True)
logger = logging.getLogger(__name__)


class APIClient:
    def __init__(
        self,
        base_url,
        max_connections=10,
        max_keepalive_connections=5,
        rate_limit=10,
    ):
        self.base_url = base_url
        self._client = httpx.AsyncClient(
            base_url=base_url,
            limits=httpx.Limits(
                max_connections=max_connections,
                max_keepalive_connections=max_keepalive_connections,
            ),
        )
        self._throttler = Throttler(rate_limit=rate_limit)

    @retry(
        stop=stop_after_attempt(5), wait=wait_exponential(multiplier=1, min=1, max=10)
    )
    async def fetch(self, endpoint="", headers=None, params=None):
        """
        Perform a GET request with caching, throttling, and retry logic.

        :param endpoint: The API endpoint to fetch (relative to the base URL).
        :param params: Query parameters as a dictionary.
        :return: JSON response data.
        """
        try:
            url = f"{self.base_url}{endpoint}"
            if params:
                query_string = "&".join(
                    f"{key}={value}" for key, value in params.items()
                )
                url += f"?{query_string}"

            async with self._throttler:
                response = await self._client.get(url, headers=headers)
                response.raise_for_status()
                data = response.json()

                self._log_usage(response)
                return data
        except Exception as e:
            logger.info(ErrorDetail.unknown("ApiClient Fetch", e))
        finally:
            await self._client.aclose()

    def _log_usage(self, response):
        rate_limit_remaining = response.headers.get("X-RateLimit-Remaining", "Unknown")
        rate_limit_reset = response.headers.get("X-RateLimit-Reset", "Unknown")
        logger.info(
            f"""Url: {self.base_url}, 
            Rate limit remaining: {rate_limit_remaining}, 
            Resets in: {rate_limit_reset}"""
        )


if __name__ == "__main__":

    async def main():
        api_client = APIClient(base_url="https://catfact.ninja/fact")
        result = await api_client.fetch("")
        print(result)

    asyncio.run(main())
