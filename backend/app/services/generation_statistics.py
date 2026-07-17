"""
Generation Statistics Service

Collects runtime statistics for TinyVerse episode generation.
"""

from __future__ import annotations

from datetime import datetime

from backend.app.schemas.generation_statistics import GenerationStatistics


class GenerationStatisticsService:
    """
    Tracks statistics for one episode generation.
    """

    def __init__(
        self,
        episode_id: str,
    ) -> None:

        self.statistics = GenerationStatistics(
            episode_id=episode_id,
            started_at=datetime.now(),
        )

    def add_image(self) -> None:
        self.statistics.image_count += 1

    def add_audio(self) -> None:
        self.statistics.audio_count += 1

    def add_video(self) -> None:
        self.statistics.video_count += 1

    def add_cache_hit(self) -> None:
        self.statistics.cache_hits += 1

    def add_cache_miss(self) -> None:
        self.statistics.cache_misses += 1

    def add_retry(self) -> None:
        self.statistics.retry_count += 1

    def set_providers(
        self,
        image: str,
        voice: str,
        video: str,
    ) -> None:

        self.statistics.image_provider = image
        self.statistics.voice_provider = voice
        self.statistics.video_provider = video

    def set_cost(
        self,
        cost: float,
    ) -> None:

        self.statistics.estimated_cost = cost

    def finish(self) -> GenerationStatistics:

        self.statistics.completed_at = datetime.now()

        self.statistics.elapsed_seconds = (
            self.statistics.completed_at - self.statistics.started_at
        ).total_seconds()

        self.statistics.status = "completed"

        return self.statistics
