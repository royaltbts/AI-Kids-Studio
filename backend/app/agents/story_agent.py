"""
Story Agent

Generates story outlines for TinyVerse episodes.
"""

from backend.app.agents.base_agent import BaseAgent
from backend.app.core.logger import logger
from backend.app.schemas.episode_context import EpisodeContext
from backend.app.schemas.story_plan import StoryPlan
from backend.app.services.prompt_service import PromptService


class StoryAgent(BaseAgent):
    """
    Generates a story outline.
    """

    def __init__(
        self,
        provider: str | None = None,
    ) -> None:
        """
        Initialize the story agent.

        If a provider is supplied, it overrides the default provider.
        """

        super().__init__(provider)

    def generate(
        self,
        context: EpisodeContext,
    ) -> EpisodeContext:
        """
        Generate the story and store it in the context.
        """

        logger.info(
            "Generating story for '%s' using provider '%s'.",
            context.topic,
            self.provider.provider_name(),
        )

        prompt = PromptService.build_story_agent_prompt(
            topic=context.topic,
            age_group=context.age_group,
            lesson_title=context.lesson.lesson_title,
            learning_objective=context.lesson.learning_objective,
        )

        context.story = self.generate_json(
            prompt=prompt,
            schema=StoryPlan,
        )

        logger.info("Story generated successfully.")

        return context
