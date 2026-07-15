"""
Rendered Music Schema

Represents rendered background music for an episode.
"""

from pydantic import BaseModel


class RenderedMusic(BaseModel):
    """
    Represents rendered background music.
    """

    title: str

    music_path: str

    duration_seconds: int

    genre: str = "Kids"

    format: str = "mp3"

    provider: str = "mock"

    status: str = "rendered"
