"""
Tests for EpisodeExporter.
"""

from datetime import datetime
from pathlib import Path

from backend.app.schemas.episode_metadata import EpisodeMetadata
from backend.app.schemas.rendered_audio import RenderedAudio
from backend.app.schemas.rendered_episode import RenderedEpisode
from backend.app.schemas.rendered_image import RenderedImage
from backend.app.schemas.rendered_music import RenderedMusic
from backend.app.schemas.rendered_video import RenderedVideo
from backend.app.services.episode_exporter import EpisodeExporter


def test_episode_exporter():
    """
    Verify that a rendered episode can be exported successfully.
    """

    metadata = EpisodeMetadata(
        episode_id="episode_001",
        topic="ABC",
        age_group="3-5",
        duration_seconds=120,
        created_at=datetime.fromisoformat("2024-01-01T00:00:00"),
        status="completed",
    )

    rendered = RenderedEpisode(
        images=[
            RenderedImage(
                scene_number=1,
                image_path="output/images/scene_001.png",
                width=1920,
                height=1080,
                status="rendered",
            )
        ],
        audio=[
            RenderedAudio(
                scene_number=1,
                title="Meet Toby",
                narration="Hello! I'm Toby Bear.",
                voice="Friendly Female",
                duration_seconds=30,
                audio_path="output/audio/scene_001.mp3",
                sample_rate=24000,
                channels=2,
                format="mp3",
                provider="mock",
                status="rendered",
            )
        ],
        music=RenderedMusic(
            title="Happy Kids Background",
            music_path="output/music/background.mp3",
            duration_seconds=120,
            genre="Kids",
            format="mp3",
            provider="mock",
            status="rendered",
        ),
        video=RenderedVideo(
            title="TinyVerse Episode",
            video_path="output/video/episode.mp4",
            duration_seconds=120,
            resolution="1920x1080",
            fps=30,
            format="mp4",
            provider="mock",
            status="rendered",
        ),
        total_duration=120,
        status="rendered",
    )

    exporter = EpisodeExporter()

    result = exporter.export(
        metadata=metadata, rendered_episode=rendered, workspace=Path("output")
    )

    assert result.success is True

    assert result.workspace.exists()

    assert result.metadata_path.exists()

    assert result.video_path == Path("output/video/episode.mp4")
