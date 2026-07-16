"""
Episode Context

Shared state passed between all AI agents.
"""

from pathlib import Path
from typing import Optional

from pydantic import BaseModel, Field

from backend.app.characters.models import Character
from backend.app.schemas.episode_assets import EpisodeAssets
from backend.app.schemas.image_prompt import ImagePrompt
from backend.app.schemas.lesson import LessonResponse
from backend.app.schemas.narration import Narration
from backend.app.schemas.scene_plan import ScenePlan
from backend.app.schemas.story_plan import StoryPlan


class EpisodeContext(BaseModel):
    """
    Shared state for a complete TinyVerse episode.
    """

    # ==========================================================
    # Episode Information
    # ==========================================================

    topic: str

    age_group: str

    provider: str = "mock"

    workspace: Path | None = None

    # ==========================================================
    # Characters
    # ==========================================================

    characters: list[Character] = Field(
        default_factory=list,
    )

    # ==========================================================
    # AI Outputs
    # ==========================================================

    lesson: Optional[LessonResponse] = None

    story: Optional[StoryPlan] = None

    scene_plan: Optional[ScenePlan] = None

    image_prompts: list[ImagePrompt] = Field(
        default_factory=list,
    )

    narrations: list[Narration] = Field(
        default_factory=list,
    )

    # ==========================================================
    # Generated Assets
    # ==========================================================

    assets: EpisodeAssets | None = None

    episode_assets: EpisodeAssets = Field(
        default_factory=EpisodeAssets,
    )
