"""
Story Agent

Generates a story outline for a TinyVerse episode.
"""

from backend.app.agents.base_agent import BaseAgent
from backend.app.schemas.episode_context import EpisodeContext
from backend.app.schemas.story_plan import StoryPlan
from backend.app.services.prompt_service import PromptService


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

        return context
