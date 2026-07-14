"""
Prompt Service

Loads prompt templates from the prompts directory
and replaces template variables.
"""

from pathlib import Path


class PromptService:
    """
    Loads prompt templates and injects variables.
    """

    BASE_DIR = Path(__file__).resolve().parents[3]
    PROMPTS_DIR = BASE_DIR / "prompts"

    @classmethod
    def load_prompt(cls, filename: str) -> str:
        """
        Load a prompt template from the prompts directory.
        """

        prompt_path = cls.PROMPTS_DIR / filename

        if not prompt_path.exists():
            raise FileNotFoundError(
                f"Prompt file not found: {prompt_path}"
            )

        return prompt_path.read_text(encoding="utf-8")

    @classmethod
    def build_lesson_prompt(
        cls,
        topic: str,
        age_group: str,
    ) -> str:
        """
        Build the lesson generation prompt.
        """

        prompt = cls.load_prompt("lesson.txt")

        prompt = prompt.replace(
            "{{topic}}",
            topic,
        )

        prompt = prompt.replace(
            "{{age_group}}",
            age_group,
        )

        return prompt

    @classmethod
    def build_story_prompt(
        cls,
        topic: str,
        age_group: str,
    ) -> str:
        """
        Build the story generation prompt.
        """

        prompt = cls.load_prompt("story.txt")

        prompt = prompt.replace(
            "{{topic}}",
            topic,
        )

        prompt = prompt.replace(
            "{{age_group}}",
            age_group,
        )

        return prompt

    @classmethod
    def build_story_agent_prompt(
        cls,
        topic: str,
        age_group: str,
        lesson_title: str,
        learning_objective: str,
    ) -> str:
        """
        Build the structured story-plan prompt.
        """

        prompt = cls.load_prompt("story_agent.txt")

        prompt = prompt.replace(
            "{{topic}}",
            topic,
        )

        prompt = prompt.replace(
            "{{age_group}}",
            age_group,
        )

        prompt = prompt.replace(
            "{{lesson_title}}",
            lesson_title,
        )

        prompt = prompt.replace(
            "{{learning_objective}}",
            learning_objective,
        )

        return prompt