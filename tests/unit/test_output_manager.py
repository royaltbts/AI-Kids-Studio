"""
Tests for Output Manager.
"""

from backend.app.storage.output_manager import OutputManager


def test_create_workspace(tmp_path):

    OutputManager.BASE_DIR = tmp_path

    workspace = OutputManager.create_episode_workspace()

    assert workspace.exists()

    assert (workspace / "images").exists()
    assert (workspace / "audio").exists()
    assert (workspace / "music").exists()
    assert (workspace / "video").exists()
    assert (workspace / "thumbnails").exists()
    assert (workspace / "logs").exists()