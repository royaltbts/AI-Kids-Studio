"""
Episode Context

Shared state passed between all AI agents.
"""

from typing import Optional

from pydantic import BaseModel, Field

from backend.app.characters.models import Character
from backend.app.schemas.lesson import LessonResponse
from backend.app.schemas.story_plan import StoryPlan
from backend.app.schemas.scene_plan import ScenePlan


class EpisodeContext(BaseModel):
    """
    Shared state for a complete TinyVerse episode.
    """

    topic: str

    age_group: str

    characters: list[Character] = Field(default_factory=list)

    lesson: Optional[LessonResponse] = None

    story: Optional[StoryPlan] = None

    scene_plan: Optional[ScenePlan] = None
