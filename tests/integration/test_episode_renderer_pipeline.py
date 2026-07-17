"""
Tests for the complete episode rendering pipeline.
"""

from backend.app.services.episode_workflow import EpisodeWorkflow


def test_episode_renderer_pipeline():
    """
    Verify a complete episode can be rendered.
    """

    result = EpisodeWorkflow().generate_episode(
        topic="Dinosaurs",
        age_group="5-7",
    )

    assert result.success is True
    assert result.workspace.exists()
    assert result.metadata_path.exists()
    assert result.video_path.exists()