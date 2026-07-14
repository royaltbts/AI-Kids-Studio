"""
Scene Agent

Generates storyboard scenes and stores them in the EpisodeContext.
"""

import json

from backend.app.providers.provider_factory import ProviderFactory
from backend.app.schemas.episode_context import EpisodeContext
from backend.app.schemas.scene import Scene
from backend.app.schemas.scene_plan import ScenePlan
from backend.app.services.prompt_service import PromptService


class SceneAgent:
    """
    Generates storyboard scenes.
    """

    def __init__(self):
        self.provider = ProviderFactory.get_provider()

    def generate(
        self,
        context: EpisodeContext,
    ) -> EpisodeContext:
        """
        Generate storyboard scenes.
        """

        if context.story is None:
            raise ValueError(
                "Story must be generated before SceneAgent runs."
            )

        prompt = PromptService.build_scene_agent_prompt(
            topic=context.topic,
            age_group=context.age_group,
            story_title=context.story.title,
            story_intro=context.story.introduction,
        )

        response = self.provider.generate(prompt)

        scene_data = json.loads(response)

        scenes = [
            Scene(**scene)
            for scene in scene_data
        ]

        scene_plan = ScenePlan(
            total_duration=sum(
                scene.duration_seconds
                for scene in scenes
            ),
            scene_count=len(scenes),
            scenes=scenes,
        )

        context.scene_plan = scene_plan

        return context