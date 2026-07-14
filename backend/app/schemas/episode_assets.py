"""
Episode Assets Schema

Contains every renderable asset required to produce
a TinyVerse episode.
"""

from pydantic import BaseModel, Field

from backend.app.schemas.scene_asset import SceneAsset


class EpisodeAssets(BaseModel):
    """
    Complete render package for one episode.
    """

    title: str = ""

    thumbnail_prompt: str = ""

    intro_music: str = ""

    outro_music: str = ""

    scenes: list[SceneAsset] = Field(default_factory=list)
