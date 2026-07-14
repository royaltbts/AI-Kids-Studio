"""
Mock Provider

Returns deterministic responses for development and unit testing.
"""

import json

from backend.app.providers.base import AIProvider


class MockProvider(AIProvider):
    """
    Mock implementation of an AI provider.
    """

    def provider_name(self) -> str:
        return "mock"

    def generate(self, prompt: str) -> str:
        """
        Generate deterministic responses for testing.
        """

        prompt = prompt.lower()

        # ==========================================================
        # Scene Agent
        # ==========================================================
        if (
            "expert storyboard artist" in prompt
            or "storyboard scenes" in prompt
            or "scene generation" in prompt
        ):
            return json.dumps(
                [
                    {
                        "scene_number": 1,
                        "title": "Meet Toby",
                        "narration": "Toby Bear wakes up excited to learn the alphabet.",
                        "visual_description": "Sunny forest with Toby waving happily.",
                        "duration_seconds": 30,
                    },
                    {
                        "scene_number": 2,
                        "title": "The Letter A",
                        "narration": "A giant red letter A appears in the sky.",
                        "visual_description": "A floating red letter A surrounded by colorful birds.",
                        "duration_seconds": 30,
                    },
                    {
                        "scene_number": 3,
                        "title": "Learning Together",
                        "narration": "Mimi Rabbit and Leo Lion help Toby practice the alphabet.",
                        "visual_description": "Friends learning with alphabet cards in a green meadow.",
                        "duration_seconds": 30,
                    },
                    {
                        "scene_number": 4,
                        "title": "Celebrate Learning",
                        "narration": "Everyone celebrates after learning the letter A.",
                        "visual_description": "Balloons, confetti and smiling forest friends.",
                        "duration_seconds": 30,
                    },
                ]
            )

        # ==========================================================
        # Story Agent
        # ==========================================================
        if "expert children's storyteller" in prompt or "story outline" in prompt:
            return json.dumps(
                {
                    "title": "ABC Adventure",
                    "introduction": (
                        "Toby Bear discovers a magical alphabet book in the forest."
                    ),
                    "moral": ("Learning is exciting when friends help each other."),
                    "scenes": [
                        "Meet Toby",
                        "Discover the Letter A",
                        "Practice Together",
                        "Celebrate Learning",
                    ],
                }
            )

        # ==========================================================
        # Lesson Agent
        # ==========================================================
        if "preschool curriculum designer" in prompt or "lesson plan" in prompt:
            return json.dumps(
                {
                    "lesson_title": "ABC Adventure",
                    "learning_objective": ("Teach children to recognize the letter A."),
                    "difficulty": "Easy",
                    "estimated_duration": 120,
                    "keywords": [
                        "Alphabet",
                        "Letter A",
                        "ABC",
                        "Learning",
                    ],
                }
            )

        # ==========================================================
        # Unknown Prompt
        # ==========================================================
        raise ValueError(f"Unsupported mock prompt:\n{prompt}")
