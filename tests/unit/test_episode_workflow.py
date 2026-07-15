"""
Tests for EpisodeWorkflow.
"""

from backend.app.workflows.episode_workflow import EpisodeWorkflow


def test_episode_workflow():
    """
    Verify that the complete episode workflow succeeds.
    """

    workflow = EpisodeWorkflow()

    result = workflow.generate_episode(
        topic="ABC",
        age_group="3-5",
    )

    assert result.success is True

    assert result.workspace.exists()

    assert result.metadata_path.exists()