"""
Rendered Video Schema

Represents the final rendered TinyVerse episode.
"""

from pydantic import BaseModel


class RenderedVideo(BaseModel):
    """
    Final rendered episode.
    """

    title: str

    video_path: str

    duration_seconds: int

    resolution: str = "1920x1080"

    fps: int = 30

    format: str = "mp4"

    provider: str = "mock"

    status: str = "rendered"
