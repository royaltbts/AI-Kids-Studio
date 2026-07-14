"""
Episode Context

Shared state passed between all AI agents.
"""

from typing import Optional

from pydantic import BaseModel

from backend.app.schemas.lesson import LessonResponse
from backend.app.schemas.story_plan import StoryPlan


class EpisodeContext(BaseModel):
    """
    Shared episode state.

    Every agent reads from this object,
    updates it,
    and returns it.
    """

    topic: str

    age_group: str

    lesson: Optional[LessonResponse] = None

    story: Optional[StoryPlan] = None