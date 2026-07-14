from backend.app.schemas.episode_context import EpisodeContext


def test_episode_context_creation():
    context = EpisodeContext(
        topic="ABC",
        age_group="3-5",
    )

    assert context.topic == "ABC"
    assert context.age_group == "3-5"
    assert context.lesson is None
    assert context.story is None
    assert context.scene_plan is None
    assert context.characters == []


def test_episode_context_independent_lists():
    context1 = EpisodeContext(
        topic="ABC",
        age_group="3-5",
    )

    context2 = EpisodeContext(
        topic="Numbers",
        age_group="4-6",
    )

    context1.characters.append("dummy")

    assert context2.characters == []
