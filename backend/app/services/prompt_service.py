"""
Prompt Service

Loads and renders prompt templates.
"""

from pathlib import Path


class PromptService:
    """
    Generic prompt rendering service.
    """

    BASE_DIR = Path(__file__).resolve().parents[3]
    PROMPTS_DIR = BASE_DIR / "prompts"

    @classmethod
    def load_prompt(cls, filename: str) -> str:
        """
        Load a prompt template from disk.
        """

        prompt_path = cls.PROMPTS_DIR / filename

        if not prompt_path.exists():
            raise FileNotFoundError(
                f"Prompt file not found: {prompt_path}"
            )

        return prompt_path.read_text(encoding="utf-8")

    @classmethod
    def render(
        cls,
        filename: str,
        **kwargs,
    ) -> str:
        """
        Render a prompt template by replacing placeholders.
        """

        prompt = cls.load_prompt(filename)

        for key, value in kwargs.items():
            prompt = prompt.replace(
                f"{{{{{key}}}}}",
                str(value),
            )

        return prompt

    @classmethod
    def build_lesson_prompt(
        cls,
        topic: str,
        age_group: str,
    ) -> str:

        return cls.render(
            "lesson.txt",
            topic=topic,
            age_group=age_group,
        )

    @classmethod
    def build_story_prompt(
        cls,
        topic: str,
        age_group: str,
    ) -> str:

        return cls.render(
            "story.txt",
            topic=topic,
            age_group=age_group,
        )

    @classmethod
    def build_story_agent_prompt(
        cls,
        topic: str,
        age_group: str,
        lesson_title: str,
        learning_objective: str,
    ) -> str:

        return cls.render(
            "story_agent.txt",
            topic=topic,
            age_group=age_group,
            lesson_title=lesson_title,
            learning_objective=learning_objective,
        )

    @classmethod
    def build_scene_agent_prompt(
        cls,
        topic: str,
        age_group: str,
        story_title: str,
        story_intro: str,
    ) -> str:

        return cls.render(
            "scene_agent.txt",
            topic=topic,
            age_group=age_group,
            story_title=story_title,
            story_intro=story_intro,
        )