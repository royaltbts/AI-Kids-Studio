"""
Unit tests for PromptService.
"""

from backend.app.services.prompt_service import PromptService


def test_load_lesson_prompt():
    prompt = PromptService.load_prompt("lesson.txt")

    assert "preschool curriculum designer" in prompt


def test_build_lesson_prompt():
    prompt = PromptService.build_lesson_prompt(
        topic="ABC",
        age_group="3-5",
    )

    assert "ABC" in prompt
    assert "3-5" in prompt
    assert "{{topic}}" not in prompt
    assert "{{age_group}}" not in prompt


def test_build_story_prompt():
    prompt = PromptService.build_story_prompt(
        topic="Colors",
        age_group="4-6",
    )

    assert "Colors" in prompt
    assert "4-6" in prompt


def test_build_story_agent_prompt():
    prompt = PromptService.build_story_agent_prompt(
        topic="ABC",
        age_group="3-5",
        lesson_title="ABC Adventure",
        learning_objective="Learn the alphabet",
    )

    assert "ABC Adventure" in prompt
    assert "Learn the alphabet" in prompt


def test_build_scene_agent_prompt():
    prompt = PromptService.build_scene_agent_prompt(
        topic="ABC",
        age_group="3-5",
        story_title="ABC Adventure",
        story_intro="Toby finds a magical alphabet book.",
    )

    assert "ABC Adventure" in prompt
    assert "Toby finds a magical alphabet book." in prompt