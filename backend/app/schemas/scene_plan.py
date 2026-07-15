"""
Scene Plan Schema

Represents the complete storyboard for a TinyVerse episode.
"""

from pydantic import BaseModel, Field

from backend.app.schemas.scene import Scene


class ScenePlan(BaseModel):
    """
    Collection of storyboard scenes with metadata.
    """

    total_duration: int = 0

    scene_count: int = 0

    scenes: list[Scene] = Field(default_factory=list)
