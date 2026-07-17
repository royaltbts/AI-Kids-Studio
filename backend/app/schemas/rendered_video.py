"""
Rendered Video Schema

Represents one rendered video clip.
"""

from pydantic import BaseModel


class RenderedVideo(BaseModel):
    """
    Represents one rendered video clip.
    """

    scene_number: int

    title: str

    video_path: str

    duration_seconds: int

    width: int

    height: int

    fps: int

    format: str = "mp4"

    codec: str = "h264"

    provider: str = "ffmpeg"

    status: str = "rendered"
