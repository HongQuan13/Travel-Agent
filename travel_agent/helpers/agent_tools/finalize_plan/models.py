from typing import List
from pydantic import BaseModel, Field, validator


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


class DeepResearchPlan(BaseModel):
    mainHeader: str = Field(
        description="The primary title or header for the generated plan, summarizing its main focus or theme."
    )
    images: List[ImageUrl] = Field(
        description="List of images about places or event inside plan",
    )
    subHeaders: List[SubHeaders] = Field(
        description="""List of subheaders inside plan""",
    )

    # @validator("images")
    # def validate_images_content(cls, value):
    #     if not isinstance(value, ImageUrl):
    #         raise ValueError("Each item in 'images' must be an ImageUrl object.")
    #     return value


class PlanGenerateNotice(BaseModel):
    plan_title: str = Field(description="Title of the deep research generated plan")
