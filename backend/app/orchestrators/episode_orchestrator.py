"""
Episode Orchestrator

Coordinates the complete TinyVerse episode generation workflow.
"""

from backend.app.agents.lesson_agent import LessonAgent
from backend.app.agents.story_agent import StoryAgent
from backend.app.schemas.episode_context import EpisodeContext


class EpisodeOrchestrator:
    """
    Coordinates all AI agents required to build an episode.
    """

    def __init__(self):
        self.lesson_agent = LessonAgent()
        self.story_agent = StoryAgent()

    def generate_episode(
        self,
        topic: str,
        age_group: str,
    ):
        """
        Generate a complete episode using a shared EpisodeContext.
        """

        context = EpisodeContext(
            topic=topic,
            age_group=age_group,
        )

        context = self.lesson_agent.generate(context)

        context = self.story_agent.generate(context)

        return context.model_dump()