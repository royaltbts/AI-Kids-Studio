"""
Prompt Service

Loads prompt templates from the prompts directory
and replaces template variables.
"""

from pathlib import Path


class PromptService:

    BASE_DIR = Path(__file__).resolve().parents[3]
    PROMPTS_DIR = BASE_DIR / "prompts"

    @classmethod
    def load_prompt(cls, filename: str) -> str:
        prompt_path = cls.PROMPTS_DIR / filename

        if not prompt_path.exists():
            raise FileNotFoundError(
                f"Prompt file not found: {prompt_path}"
            )

        return prompt_path.read_text(encoding="utf-8")

    @classmethod
    def build_story_prompt(
        cls,
        topic: str,
        age_group: str,
    ) -> str:

        prompt = cls.load_prompt("story.txt")

        prompt = prompt.replace("{{topic}}", topic)
        prompt = prompt.replace("{{age_group}}", age_group)

        return prompt

    @classmethod
    def build_lesson_prompt(
        cls,
        topic: str,
        age_group: str,
    ) -> str:

        prompt = cls.load_prompt("lesson.txt")

        prompt = prompt.replace("{{topic}}", topic)
        prompt = prompt.replace("{{age_group}}", age_group)

        return prompt