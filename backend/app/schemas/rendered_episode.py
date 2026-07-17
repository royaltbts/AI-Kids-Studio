"""
Rendered Episode Schema

Represents all rendered media for one episode.
"""

from pydantic import BaseModel, Field

from backend.app.schemas.rendered_audio import RenderedAudio
from backend.app.schemas.rendered_image import RenderedImage
from backend.app.schemas.rendered_music import RenderedMusic
from backend.app.schemas.rendered_video import RenderedVideo


class RenderedEpisode(BaseModel):
    """
    Complete rendered episode.
    """

    # Images
    images: list[RenderedImage] = Field(default_factory=list)

    # Narration
    audio: list[RenderedAudio] = Field(default_factory=list)

    # Scene videos
    videos: list[RenderedVideo] = Field(default_factory=list)

    # Background music
    music: RenderedMusic | None = None

    # Episode metadata
    episode_title: str = ""

    total_duration: int = 0

    status: str = "rendered"
