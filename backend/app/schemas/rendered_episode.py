"""
Rendered Episode Schema

Represents all rendered media assets.
"""

from pydantic import BaseModel, Field

from backend.app.schemas.rendered_audio import RenderedAudio
from backend.app.schemas.rendered_image import RenderedImage


class RenderedEpisode(BaseModel):
    """
    Final rendered assets for an episode.
    """

    images: list[RenderedImage] = Field(default_factory=list)

    audio: list[RenderedAudio] = Field(default_factory=list)

    total_duration: int = 0

    episode_title: str = ""

    thumbnail_path: str = ""

    status: str = "rendered"
