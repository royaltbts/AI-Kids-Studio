"""
Rendered Music Schema

Represents rendered background music for an episode.
"""

from pydantic import BaseModel


class RenderedMusic(BaseModel):
    """
    Represents rendered background music.
    """

    # Music information
    title: str

    # Output file
    music_path: str

    # Duration (seconds)
    duration_seconds: int

    # Music metadata
    genre: str = "Kids"

    format: str = "mp3"

    provider: str = "mock"

    # Rendering status
    status: str = "rendered"
