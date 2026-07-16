"""
CLI tests.
"""


from backend.app.cli.generate_episode import main


def test_cli(monkeypatch):
    """
    Verify CLI execution using the mock provider.
    """

    monkeypatch.setenv("AI_PROVIDER", "mock")

    monkeypatch.setattr(
        "sys.argv",
        [
            "generate_episode",
            "--topic",
            "ABC",
            "--age-group",
            "3-5",
            "--provider",
            "mock",
        ],
    )

    assert main() == 0
