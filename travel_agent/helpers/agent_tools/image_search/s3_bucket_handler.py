import os
import logging
import time
import boto3
import requests
from dotenv import load_dotenv
from botocore.exceptions import ClientError


from backend.src.constant.error_constant import ErrorDetail
from backend.src.constant.info_constant import InfoDetail

logging.basicConfig(level=logging.INFO, force=True)
logger = logging.getLogger(__name__)
load_dotenv()


class S3BucketHandler:
    _instance = None
    _source_bucket = "travel-agent-origin-image"
    _dest_bucket = "travel-agent-resize-image"

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(S3BucketHandler, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        self._check_env()
        self._s3 = self._config()
        logger.info(InfoDetail.class_initialize("S3BucketHandler"))

    def _check_env(self):
        access_key_id = os.getenv("AWS_ACCESS_KEY")
        secret_access_key = os.getenv("AWS_SECRET_KEY")

        if access_key_id is None or secret_access_key is None:
            raise ValueError(f"Unable to access s3 aws credentials in .env file")

        self._access_key_id = access_key_id
        self._secret_access_key = secret_access_key

    def _config(self):
        return boto3.client(
            "s3",
            aws_access_key_id=self._access_key_id,
            aws_secret_access_key=self._secret_access_key,
        )

    def image_process(self, image_url: str):
        object_key = self._put_object(image_url)
        transformed_image = self._get_object(object_key)
        return transformed_image

    def _put_object(self, image_url: str):

        try:
            response = requests.get(image_url)
            response.raise_for_status()

            image_key = image_url.strip().split("?")[0].split("/")[-1]

            self._s3.put_object(
                Bucket=self._source_bucket,
                Key=image_key,
                Body=response.content,
                ContentType=response.headers["Content-Type"],
            )

            self._wait_until_object_exists(self._source_bucket, image_key)

            logger.info("S3 bucket - New object uploaded")
            return image_key
        except ClientError as e:
            error_code = e.response["Error"]["Code"]
            if error_code == "PreconditionFailed":
                print("\tConditional write failed: Precondition failed")
            else:
                logger.error(ErrorDetail.unknown("Aws upload image", error_code))
                raise

    def _get_object(self, object_key: str, expiration: int = 172800):
        try:
            self._wait_until_object_exists(self._dest_bucket, object_key)

            presigned_url = self._s3.generate_presigned_url(
                "get_object",
                Params={"Bucket": self._dest_bucket, "Key": object_key},
                ExpiresIn=expiration,
            )

            return presigned_url
        except ClientError as e:
            logger.error(ErrorDetail.unknown("Aws get image", e))
            raise

    def _wait_until_object_exists(
        self, bucket_name, object_name, max_wait_time=20, interval=5
    ):
        start_time = time.time()
        while time.time() - start_time < max_wait_time:
            try:
                self._s3.head_object(Bucket=bucket_name, Key=object_name)
                logger.info(f"Object '{object_name}' exists in bucket '{bucket_name}'.")
                return
            except ClientError as e:
                if e.response["Error"]["Code"] != "404":
                    raise
            time.sleep(interval)
        raise TimeoutError(
            f"Object '{object_name}' did not appear in bucket '{bucket_name}' within {max_wait_time} seconds."
        )


if __name__ == "__main__":
    s3_handler = S3BucketHandler()
    img_url = "https://images.twinkl.co.uk/tw1n/image/private/t_630/u/ux/leopard-515509-1920_ver_1.jpg"
    s3_handler.image_process(img_url)
