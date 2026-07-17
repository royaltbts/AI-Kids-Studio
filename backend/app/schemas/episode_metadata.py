"""
Episode Metadata Schema.
"""

from datetime import datetime

from pydantic import BaseModel

from backend.app.schemas.generation_statistics import (
    GenerationStatistics,
)


class EpisodeMetadata(BaseModel):
    """
    Metadata describing a generated TinyVerse episode.
    """

    #
    # Episode Information
    #

    episode_id: str

    topic: str

    age_group: str

    created_at: datetime

    duration_seconds: int

    status: str = "completed"

    #
    # Output Assets
    #

    video_path: str = ""

    thumbnail_path: str = ""

    #
    # Runtime Statistics
    #

    statistics: GenerationStatistics | None = None
