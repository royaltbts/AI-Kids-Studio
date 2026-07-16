"""
Episode Workflow

Coordinates the complete TinyVerse episode generation pipeline.
"""

from datetime import datetime

from backend.app.agents.image_prompt_agent import ImagePromptAgent
from backend.app.agents.lesson_agent import LessonAgent
from backend.app.agents.narration_agent import NarrationAgent
from backend.app.agents.scene_agent import SceneAgent
from backend.app.agents.story_agent import StoryAgent
from backend.app.schemas.episode_context import EpisodeContext
from backend.app.schemas.episode_metadata import EpisodeMetadata
from backend.app.schemas.export_result import ExportResult
from backend.app.services.asset_assembler import AssetAssembler
from backend.app.services.episode_exporter import EpisodeExporter
from backend.app.services.media_pipeline import MediaPipeline


class EpisodeWorkflow:
    """
    Coordinates the complete episode generation workflow.
    """

    def generate_episode(
        self,
        topic: str,
        age_group: str,
    ) -> ExportResult:
        """
        Generate a complete TinyVerse episode.
        """

        context = EpisodeContext(
            topic=topic,
            age_group=age_group,
        )

        context = LessonAgent().generate(context)

        context = StoryAgent().generate(context)

        context = SceneAgent().generate(context)

        context = ImagePromptAgent().generate(context)

        context = NarrationAgent().generate(context)

        assets = AssetAssembler.build(context)

        rendered = MediaPipeline().render(
            assets,
        )

        metadata = EpisodeMetadata(
            episode_id="episode_001",
            topic=context.topic,
            age_group=context.age_group,
            created_at=datetime.now(),
            duration_seconds=rendered.total_duration,
            status="completed",
        )

        return EpisodeExporter().export(
            metadata=metadata,
            rendered_episode=rendered,
        )
