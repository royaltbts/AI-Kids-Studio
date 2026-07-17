"""
Tests for EpisodeComposer.
"""

from pathlib import Path

from backend.app.services.episode_composer import EpisodeComposer


def test_episode_composer():
    """
    Verify EpisodeComposer can combine scene videos.
    """

    workspace = Path("output/episode_test")

    workspace.mkdir(
        parents=True,
        exist_ok=True,
    )

    video_dir = workspace / "video"

    video_dir.mkdir(
        exist_ok=True,
    )

    #
    # This test will be expanded later with generated
    # scene videos. For now we simply verify that the
    # service can be instantiated.
    #

    composer = EpisodeComposer()

    assert composer is not None
