import os
import logging
import cloudinary
import cloudinary.uploader
from cloudinary.utils import cloudinary_url
from dotenv import load_dotenv

from backend.src.constant.error_constant import ErrorDetail
from backend.src.constant.info_constant import InfoDetail

logging.basicConfig(level=logging.INFO, force=True)
logger = logging.getLogger(__name__)
load_dotenv()


class CloudinaryHandler:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(CloudinaryHandler, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        self._check_env()
        self._config()
        logger.info(InfoDetail.class_initialize("CloudinaryHandler"))

    def _check_env(self):
        api_key = os.getenv("CLOUDINARY_API_KEY")
        api_secret = os.getenv("CLOUDINARY_API_SECRET")
        cloud_name = os.getenv("CLOUDINARY_NAME")

        if api_key is None or api_secret is None or cloud_name is None:
            raise ValueError(f"Unable to access cloudinary credentials in .env file")

        self._api_key = api_key
        self._api_secret = api_secret
        self._cloud_name = cloud_name

    def _config(self):
        cloudinary.config(
            cloud_name=self._cloud_name,
            api_key=self._api_key,
            api_secret=self._api_secret,
            secure=True,
        )

    def upload_image(self, image_url: str) -> str:
        try:
            upload_result = cloudinary.uploader.upload(
                image_url,
                folder="travel-agent",
                format="png",
                transformation=[
                    {
                        "width": 800,
                        "height": 600,
                        "crop": "limit",
                    },
                    {
                        "quality": "auto",
                        "fetch_format": "auto",
                    },
                ],
            )

            optimized_url, _ = cloudinary_url(
                upload_result["public_id"],
                width=650,
                height=365,
                crop="auto",
                gravity="auto",
                fetch_format="auto",
                quality="auto",
            )
        except Exception as error:
            logger.error(ErrorDetail.unknown("upload_image", error))

        return optimized_url


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, force=True)
    logger = logging.getLogger(__name__)

    image_search = CloudinaryHandler()
    url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS2L7RSlOxJMxCdE_nAbQOQV3qMvE-r4HYQRGkhx8ibmz9BITOkvmRSBeG9Xg&s"
    main_content = image_search.upload_image(url)
    logger.info(main_content)
