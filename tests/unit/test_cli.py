"""
Tests for TinyVerse CLI.
"""

from backend.app.cli.generate_episode import main


def test_cli(monkeypatch):
    """
    Verify CLI execution.
    """

    monkeypatch.setattr(
        "sys.argv",
        [
            "generate_episode",
            "--topic",
            "ABC",
            "--age-group",
            "3-5",
        ],
    )

    assert main() == 0
