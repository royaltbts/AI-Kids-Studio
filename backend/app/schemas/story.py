from pydantic import BaseModel


class StoryRequest(BaseModel):
    topic: str
    age_group: str = "3-5"


class StoryResponse(BaseModel):
    title: str
    story: str
    moral: str