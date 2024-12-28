from typing import List
from pydantic import BaseModel, Field, validator
from langchain_core.runnables import RunnableConfig


class Review(BaseModel):
    author_name: str = Field(description="The name of the author who wrote the review.")
    rating: int = Field(
        description="The rating given by the author, typically a number between 1 and 5."
    )
    relative_time_description: str = Field(
        description="A description of when the review was posted (e.g., '2 days ago')."
    )
    text: str = Field(
        description="The content or body of the review written by the author."
    )


class Place(BaseModel):
    placeName: str = Field(description="The name of the place or event")
    address: str = Field(description="The geographical address of the place or event.")
    description: str = Field(description="A brief summary of the place or event.")
    current_opening_hours: str = Field(
        description="The current opening hours of the place or event."
    )
    geometry: str = Field(
        description="Geographical coordinates (latitude and longitude) of the place(e.g., 1.3521,103.8198)."
    )
    reviews: List[Review] = Field(
        description="A list of reviews or feedback about the place."
    )
    international_phone_number: str = Field(
        description="The international phone number for contacting the place.",
        default="",
    )


class SubHeaders(BaseModel):
    title: str = Field(description="A short descritive title")
    places: List[Place] = Field(
        description="A list of Place objects associated with that subheader."
    )


class ImageUrl(BaseModel):
    image_url: str = Field(description="Image url associated with the place or event")

    @validator("image_url")
    def validate_url(cls, value):
        if not value.startswith(("http://", "https://")):
            raise ValueError(
                "The 'image_url' must be a valid URL starting with 'http://' or 'https://'."
            )
        return value


class FinalItinerary(BaseModel):
    mainHeader: str = Field(
        description="The primary title or header for the final itinerary, summarizing its main focus or theme."
    )
    images: List[ImageUrl] = Field(
        description="List of images about places or event inside itinerary",
    )
    subHeaders: List[SubHeaders] = Field(
        description="""List of subheaders inside itinerary""",
    )
    config: RunnableConfig


class SucessfulItineraryNotice(BaseModel):
    itinerary_title: str = Field(description="Title of the final itinerary")
