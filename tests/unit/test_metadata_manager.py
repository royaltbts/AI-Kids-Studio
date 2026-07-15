"""
Tests for MetadataManager.
"""

from datetime import datetime

from backend.app.schemas.episode_metadata import EpisodeMetadata
from backend.app.services.metadata_manager import MetadataManager
from backend.app.storage.output_manager import OutputManager


def test_metadata_manager():
    """
    Verify that episode metadata can be saved,
    loaded, and validated successfully.
    """

    workspace = OutputManager.create_episode_workspace()

    metadata = EpisodeMetadata(
        episode_id="episode_001",
        topic="ABC",
        age_group="3-5",
        duration_seconds=120,
        created_at=datetime.fromisoformat("2024-01-01T00:00:00"),
        status="completed",
    )

    metadata_path = MetadataManager.save(
        workspace,
        metadata,
    )

    assert metadata_path.exists()

    assert MetadataManager.exists(
        workspace,
    )

    loaded = MetadataManager.load(
        workspace,
    )

    assert loaded.episode_id == "episode_001"

    assert loaded.topic == "ABC"

    assert loaded.age_group == "3-5"

    assert loaded.duration_seconds == 120

    assert loaded.status == "completed"

    assert loaded.video_path == ""

    assert loaded.thumbnail_path == ""

    assert loaded.created_at == datetime.fromisoformat("2024-01-01T00:00:00")
