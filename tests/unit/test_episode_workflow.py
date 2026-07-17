"""
Tests for EpisodeWorkflow.
"""

from backend.app.services.episode_workflow import EpisodeWorkflow


def test_episode_workflow() -> None:
    """
    Verify that the complete episode workflow succeeds using
    mock providers.
    """

    workflow = EpisodeWorkflow()

    result = workflow.generate_episode(
        topic="ABC",
        age_group="3-5",
        provider="mock",
    )

    assert result.success is True
    assert result.workspace.exists()
    assert result.metadata_path.exists()
    assert result.video_path.exists()
