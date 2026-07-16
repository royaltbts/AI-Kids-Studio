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
from backend.app.storage.output_manager import OutputManager


class EpisodeWorkflow:
    """
    Coordinates the complete episode generation workflow.
    """

    def generate_episode(
        self,
        topic: str,
        age_group: str,
        provider: str | None = None,
    ) -> ExportResult:
        """
        Generate a complete TinyVerse episode.
        """

        #
        # Create Episode Workspace
        #

        workspace = OutputManager.create_episode_workspace()

        #
        # Shared Context
        #

        context = EpisodeContext(
            topic=topic,
            age_group=age_group,
            provider=provider or "mock",
            workspace=workspace,
        )

        #
        # AI Pipeline
        #

        context = LessonAgent(provider).generate(context)

        context = StoryAgent(provider).generate(context)

        context = SceneAgent(provider).generate(context)

        context = ImagePromptAgent(provider).generate(context)

        context = NarrationAgent(provider).generate(context)

        #
        # Assemble Assets
        #

        assets = AssetAssembler.build(
            context,
        )

        #
        # Render Media
        #

        rendered = MediaPipeline().render(
            workspace=workspace,
            assets=assets,
        )

        #
        # Metadata
        #

        metadata = EpisodeMetadata(
            episode_id=workspace.name,
            topic=context.topic,
            age_group=context.age_group,
            created_at=datetime.now(),
            duration_seconds=rendered.total_duration,
            status="completed",
        )

        #
        # Export
        #

        return EpisodeExporter().export(
            workspace=workspace,
            metadata=metadata,
            rendered_episode=rendered,
        )
