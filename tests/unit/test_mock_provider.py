"""
Unit tests for MockProvider.
"""

import json

from backend.app.providers.mock_provider import MockProvider


def test_generate_lesson():

    provider = MockProvider()

    response = provider.generate(
        "Create a lesson plan"
    )

    lesson = json.loads(response)

    assert "lesson_title" in lesson
    assert "learning_objective" in lesson


def test_generate_story():

    provider = MockProvider()

    response = provider.generate(
        "story outline"
    )

    story = json.loads(response)

    assert "title" in story
    assert "introduction" in story


def test_generate_scene():

    provider = MockProvider()

    response = provider.generate(
        "storyboard scenes"
    )

    scenes = json.loads(response)

    assert isinstance(scenes, list)

    assert len(scenes) > 0

    assert "scene_number" in scenes[0]