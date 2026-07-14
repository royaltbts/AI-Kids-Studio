from pydantic import BaseModel, Field


class StoryRequest(BaseModel):

    topic: str = Field(
        ...,
        description="Educational topic",
        examples=["ABC"],
    )

    age_group: str = Field(
        default="3-5",
        examples=["3-5"],
    )


class StoryResponse(BaseModel):

    title: str

    story: str

    moral: str
