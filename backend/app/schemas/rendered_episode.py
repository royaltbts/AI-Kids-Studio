"""
Rendered Episode Schema

Represents all rendered media assets for an episode.
"""

from pydantic import BaseModel, Field

from backend.app.schemas.rendered_audio import RenderedAudio
from backend.app.schemas.rendered_image import RenderedImage
from backend.app.schemas.rendered_music import RenderedMusic
from backend.app.schemas.rendered_video import RenderedVideo


class RenderedEpisode(BaseModel):
    """
    Final rendered assets for an episode.
    """

    images: list[RenderedImage] = Field(
        default_factory=list,
    )

    audio: list[RenderedAudio] = Field(
        default_factory=list,
    )

    music: RenderedMusic | None = None

    video: RenderedVideo | None = None

    total_duration: int = 0

    episode_title: str = ""

    thumbnail_path: str = ""

    status: str = "rendered"
