"""
Mock Provider

Returns deterministic responses for development and unit testing.
"""

import json
import re

from backend.app.providers.base import AIProvider


class MockProvider(AIProvider):
    """
    Mock implementation of an AI provider.
    """

    def _extract_value(
        self,
        prompt: str,
        label: str,
        default: str = "",
    ) -> str:
        """
        Extract a value following a label in the prompt.
        """

        pattern = rf"{label}:\s*(.+)"

        match = re.search(
            pattern,
            prompt,
            re.IGNORECASE,
        )

        if match:
            return match.group(1).strip()

        return default

    def _extract_scene_number(
        self,
        prompt: str,
    ) -> int:
        """
        Extract the scene number from the prompt.
        """

        value = self._extract_value(
            prompt,
            "Scene Number",
            "1",
        )

        try:
            return int(value)
        except ValueError:
            return 1

    def provider_name(self) -> str:
        return "mock"

    def generate(self, prompt: str) -> str:
        """
        Generate deterministic responses for testing.
        """

        prompt = prompt.lower()

        # ==========================================================
        # Lesson Agent
        # ==========================================================
        if "preschool curriculum designer" in prompt or "lesson plan" in prompt:
            return json.dumps(
                {
                    "lesson_title": "ABC Adventure",
                    "learning_objective": "Teach children to recognize the letter A.",
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
        # Scene Agent
        # ==========================================================
        if (
            "expert storyboard artist" in prompt
            or "storyboard scenes" in prompt
            or "scene generation" in prompt
        ):
            return json.dumps(
                {
                    "total_duration": 120,
                    "scene_count": 4,
                    "scenes": [
                        {
                            "scene_number": 1,
                            "title": "Meet Toby",
                            "narration": (
                                "Toby Bear wakes up excited to learn the alphabet."
                            ),
                            "visual_description": (
                                "Sunny forest with Toby waving happily."
                            ),
                            "duration_seconds": 30,
                        },
                        {
                            "scene_number": 2,
                            "title": "The Letter A",
                            "narration": ("A giant red letter A appears in the sky."),
                            "visual_description": (
                                "A floating red letter A surrounded by colorful birds."
                            ),
                            "duration_seconds": 30,
                        },
                        {
                            "scene_number": 3,
                            "title": "Learning Together",
                            "narration": (
                                "Mimi Rabbit and Leo Lion help Toby practice the alphabet."
                            ),
                            "visual_description": (
                                "Friends learning with alphabet cards."
                            ),
                            "duration_seconds": 30,
                        },
                        {
                            "scene_number": 4,
                            "title": "Celebrate Learning",
                            "narration": (
                                "Everyone celebrates after learning the letter A."
                            ),
                            "visual_description": ("Balloons and confetti."),
                            "duration_seconds": 30,
                        },
                    ],
                }
            )

        # ==========================================================
        # Image Prompt Agent
        # ==========================================================
        if (
            "children's animation concept artist" in prompt
            or "image generation prompt" in prompt
        ):

            scene_number = self._extract_scene_number(prompt)

            title = self._extract_value(
                prompt,
                "Scene Title",
                "Scene",
            )

            return json.dumps(
                {
                    "scene_number": scene_number,
                    "title": title,
                    "prompt": (
                        f"Pixar-quality 3D preschool animation of "
                        f"{title}. Bright colorful forest, Toby Bear, "
                        f"cinematic lighting, vibrant colors, "
                        f"16:9 composition."
                    ),
                    "negative_prompt": ("blurry, low quality, dark, scary, violence"),
                    "style": "Pixar 3D",
                    "aspect_ratio": "16:9",
                }
            )

        # ==========================================================
        # Narration Agent
        # ==========================================================
        if "expert preschool storyteller" in prompt or "voice-over" in prompt:

            scene_number = self._extract_scene_number(prompt)

            title = self._extract_value(
                prompt,
                "Scene Title",
                "Scene",
            )

            return json.dumps(
                {
                    "scene_number": scene_number,
                    "title": title,
                    "narration": (
                        f"Welcome to {title}! "
                        "Let's learn together with Toby Bear and friends."
                    ),
                    "voice": "Friendly Female",
                    "language": "English",
                    "duration_seconds": 30,
                }
            )

        # ==========================================================
        # Unknown Prompt
        # ==========================================================
        raise ValueError(f"Unsupported mock prompt:\n{prompt}")
