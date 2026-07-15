from typing import List

from pydantic import BaseModel


class StoryPlan(BaseModel):
    """
    High-level story structure generated from a lesson.
    """

    title: str

    introduction: str

    moral: str

    scenes: List[str]
