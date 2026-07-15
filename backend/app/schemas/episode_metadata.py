"""
Episode Metadata Schema.
"""

from datetime import datetime

from pydantic import BaseModel


class EpisodeMetadata(BaseModel):
    """
    Metadata describing a generated episode.
    """

    episode_id: str

    topic: str

    age_group: str

    created_at: datetime

    duration_seconds: int

    video_path: str = ""

    thumbnail_path: str = ""

    status: str = "completed"
