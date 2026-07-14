"""
Scene Agent

Generates storyboard scenes for a TinyVerse episode.
"""

from backend.app.agents.base_agent import BaseAgent
from backend.app.schemas.episode_context import EpisodeContext
from backend.app.schemas.scene_plan import ScenePlan
from backend.app.services.prompt_service import PromptService


class SceneAgent(BaseAgent):
    """
    Generates storyboard scenes.
    """

    def __init__(self):
        super().__init__()

    def generate(
        self,
        context: EpisodeContext,
    ) -> EpisodeContext:
        """
        Generate storyboard scenes and store them in the context.
        """

        prompt = PromptService.build_scene_agent_prompt(
            topic=context.topic,
            age_group=context.age_group,
            story_title=context.story.title,
            story_intro=context.story.introduction,
        )

        context.scene_plan = self.generate_json(
            prompt=prompt,
            schema=ScenePlan,
        )

        return context
