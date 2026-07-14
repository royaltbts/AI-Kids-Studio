"""
Episode Orchestrator

Coordinates the complete TinyVerse episode generation workflow.
"""

from backend.app.agents.lesson_agent import LessonAgent
from backend.app.agents.story_agent import StoryAgent
from backend.app.agents.scene_agent import SceneAgent
from backend.app.schemas.episode_context import EpisodeContext
from backend.app.characters.character_service import CharacterService
from backend.app.agents.image_prompt_agent import ImagePromptAgent


class EpisodeOrchestrator:
    """
    Coordinates all AI agents required to build an episode.
    """

    def __init__(self):
        self.lesson_agent = LessonAgent()
        self.story_agent = StoryAgent()
        self.scene_agent = SceneAgent()
        self.image_prompt_agent = ImagePromptAgent()

    def generate_episode(
        self,
        topic: str,
        age_group: str,
    ):
        """
        Generate a complete TinyVerse episode.
        """

        context = EpisodeContext(
            topic=topic,
            age_group=age_group,
            characters=CharacterService.list_characters(),
        )

        context = self.lesson_agent.generate(context)

        context = self.story_agent.generate(context)

        context = self.scene_agent.generate(context)

        context = self.image_prompt_agent.generate(context)

        return context.model_dump()
