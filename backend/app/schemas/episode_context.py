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
from backend.app.schemas.episode_assets import EpisodeAssets
from pydantic import BaseModel, Field

from backend.app.schemas.image_prompt import ImagePrompt
from backend.app.schemas.narration import Narration
from backend.app.schemas.episode_assets import EpisodeAssets


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
    assets: EpisodeAssets | None = None
    image_prompts: list[ImagePrompt] = Field(default_factory=list)
    narrations: list[Narration] = Field(default_factory=list)
    episode_assets: EpisodeAssets = Field(default_factory=EpisodeAssets)
