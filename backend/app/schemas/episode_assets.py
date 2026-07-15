"""
Episode Assets Schema

Represents all renderable assets for one episode.
"""

from pydantic import BaseModel, Field

from backend.app.schemas.scene_asset import SceneAsset


class EpisodeAssets(BaseModel):
    """
    Collection of renderable assets for an episode.
    """

    title: str = ""

    thumbnail_prompt: str = ""

    intro_music: str = ""

    outro_music: str = ""

    total_duration: int = 0

    scenes: list[SceneAsset] = Field(default_factory=list)
