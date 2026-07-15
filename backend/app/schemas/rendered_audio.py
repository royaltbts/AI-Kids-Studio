"""
Rendered Audio Schema

Represents a generated narration audio asset.
"""

from pydantic import BaseModel


class RenderedAudio(BaseModel):
    """
    Represents a rendered narration audio file.
    """

    scene_number: int

    title: str

    narration: str

    voice: str

    duration_seconds: int

    audio_path: str

    sample_rate: int = 24000

    channels: int = 2

    format: str = "mp3"

    provider: str = "mock"

    status: str = "rendered"