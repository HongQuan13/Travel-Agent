import logging
import os
from typing import Literal
import googlemaps
from dotenv import load_dotenv

from backend.src.constant.info_constant import InfoDetail

logging.basicConfig(level=logging.INFO, force=True)
logger = logging.getLogger(__name__)
load_dotenv()


class GoogleMapHandler:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(GoogleMapHandler, cls).__new__(cls)
            cls._gmaps_client = None
        return cls._instance

    def __init__(self):
        self._check_env()
        self._gmaps_client = self._config()
        logger.info(InfoDetail.class_initialize("GoogleMapHandler"))

    def _check_env(self):
        api_key = os.getenv("GOOGLEMAP_API_KEY")

        if api_key is None:
            raise ValueError(f"Unable to access googlemap credentials in .env file")

        self._api_key = api_key

    def _config(self):
        return googlemaps.Client(key=self._api_key)

    def get_geocode(self, place_name: str):
        geocode_result = self._gmaps_client.geocode(place_name)[0]
        data = {
            "formatted_address": geocode_result["formatted_address"],
            "geometry": f"{geocode_result['geometry']['location']['lat']},{geocode_result['geometry']['location']['lng']}",
        }
        return data

    def get_distance(
        self,
        origin: str,
        destination: str,
        mode: Literal["driving", "walking", "transit", "bicycling"] = "driving",
    ):
        distance_matrix = self._gmaps_client.distance_matrix(
            origins=origin,
            destinations=destination,
            mode=mode,
        )
        dist_data = distance_matrix["rows"][0]["elements"][0]
        data = {
            "distance": dist_data["distance"]["text"],
            "duration": dist_data["duration"]["text"],
        }
        return data

    def get_detail_place(self, place_name: str):
        places = self._gmaps_client.places(query=place_name)
        place_id = places["results"][0]["place_id"]

        response = self._gmaps_client.place(
            place_id,
            fields=None,
            reviews_no_translations=False,
            reviews_sort="most_relevant",
        )
        place_data = response["result"]

        formated_data = {
            "business_status": place_data["business_status"],
            "open_now": place_data["current_opening_hours"]["open_now"],
            "current_opening_hours": place_data["current_opening_hours"][
                "weekday_text"
            ],
            "editorial_summary": place_data["editorial_summary"]["overview"],
            "formatted_address": place_data["formatted_address"],
            "geometry": f"{place_data['geometry']['location']['lat']},{place_data['geometry']['location']['lng']}",
            "international_phone_number": place_data["international_phone_number"],
            "name": place_data["name"],
            "reviews": place_data["reviews"],
        }

        return formated_data


if __name__ == "__main__":
    gmap = GoogleMapHandler()
    response = gmap.get_detail_place("NTU singapore")
    logger.info(response)
