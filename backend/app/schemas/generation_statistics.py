"""
Generation Statistics Schema

Represents execution statistics for a TinyVerse episode.
"""

from datetime import datetime

from pydantic import BaseModel


class GenerationStatistics(BaseModel):
    """
    Statistics collected during episode generation.
    """

    episode_id: str

    started_at: datetime

    completed_at: datetime | None = None

    elapsed_seconds: float = 0.0

    image_count: int = 0

    audio_count: int = 0

    video_count: int = 0

    cache_hits: int = 0

    cache_misses: int = 0

    retry_count: int = 0

    estimated_cost: float = 0.0

    image_provider: str = ""

    voice_provider: str = ""

    video_provider: str = ""

    status: str = "running"
