"""
Unit tests for MockProvider.
"""

import json

from backend.app.providers.mock_provider import MockProvider


def test_generate_lesson():

    provider = MockProvider()

    response = provider.generate("lesson plan")

    lesson = json.loads(response)

    assert lesson["lesson_title"] == "ABC Adventure"


def test_generate_story():

    provider = MockProvider()

    response = provider.generate("story outline")

    story = json.loads(response)

    assert story["title"] == "ABC Adventure"
    assert len(story["scenes"]) == 4


def test_generate_scene():

    provider = MockProvider()

    response = provider.generate("storyboard scenes")

    scene_plan = json.loads(response)

    assert scene_plan["scene_count"] == 4

    assert scene_plan["total_duration"] == 120

    assert len(scene_plan["scenes"]) == 4

    assert scene_plan["scenes"][0]["scene_number"] == 1
