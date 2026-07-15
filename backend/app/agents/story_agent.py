"""
Story Agent

Generates a story outline for a TinyVerse episode.
"""

from backend.app.agents.base_agent import BaseAgent
from backend.app.schemas.episode_context import EpisodeContext
from backend.app.schemas.story_plan import StoryPlan
from backend.app.services.prompt_service import PromptService
from backend.app.core.logger import logger


class StoryAgent(BaseAgent):
    """
    Generates a story outline.
    """

    def __init__(self):
        super().__init__()

    def generate(
        self,
        context: EpisodeContext,
    ) -> EpisodeContext:
        """
        Generate the story and store it in the context.
        """

        assert (
            context.lesson is not None
        ), "Lesson context is required for story generation"

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
        logger.info(
            "Generating story for '%s'",
            context.topic,
        )
        logger.info("Story generated successfully.")

        return context
