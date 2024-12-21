from typing import List
from pydantic import BaseModel, Field, validator
from langchain_core.runnables import RunnableConfig


class Place(BaseModel):
    placeName: str = Field(description="The name of the place or event")
    address: str = Field(description="The geographical address of the place or event.")
    description: str = Field(description="A brief summary of the place or event.")


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
