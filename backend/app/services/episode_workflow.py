"""
Episode Workflow

Coordinates the complete TinyVerse episode generation pipeline.
"""

from datetime import datetime
from pathlib import Path

from backend.app.agents.image_prompt_agent import ImagePromptAgent
from backend.app.agents.lesson_agent import LessonAgent
from backend.app.agents.narration_agent import NarrationAgent
from backend.app.agents.scene_agent import SceneAgent
from backend.app.agents.story_agent import StoryAgent
from backend.app.schemas.episode_context import EpisodeContext
from backend.app.schemas.episode_metadata import EpisodeMetadata
from backend.app.schemas.export_result import ExportResult
from backend.app.services.asset_assembler import AssetAssembler
from backend.app.services.episode_composer import EpisodeComposer
from backend.app.services.episode_exporter import EpisodeExporter
from backend.app.services.media_pipeline import MediaPipeline
from backend.app.services.progress_tracker import ProgressTracker
from backend.app.storage.output_manager import OutputManager


class EpisodeWorkflow:
    """
    Coordinates the complete episode generation workflow.
    """

    def __init__(self) -> None:
        """
        Initialize workflow services.
        """

        self.progress = ProgressTracker()

        stages = [
            "Lesson",
            "Story",
            "Scene Plan",
            "Image Prompts",
            "Narration",
            "Asset Assembly",
            "Media Rendering",
            "Episode Composition",
            "Export",
        ]

        for stage in stages:
            self.progress.add_stage(stage)

    def _complete_stage(self, stage: str) -> None:
        """
        Mark a workflow stage as complete and display progress.
        """

        self.progress.complete_stage(stage)
        self.progress.print_progress()
        print()

    def generate_episode(
        self,
        topic: str,
        age_group: str,
        provider: str | None = None,
    ) -> ExportResult:
        """
        Generate a complete TinyVerse episode.
        """

        print("=" * 60)
        print("TinyVerse Kids Studio")
        print("=" * 60)
        print(f"Topic      : {topic}")
        print(f"Age Group  : {age_group}")
        print()

        #
        # Create workspace
        #

        workspace = OutputManager.create_episode_workspace()

        #
        # Shared context
        #

        context = EpisodeContext(
            topic=topic,
            age_group=age_group,
            provider=provider or "mock",
            workspace=workspace,
        )

        #
        # Lesson
        #

        context = LessonAgent(provider).generate(context)
        self._complete_stage("Lesson")

        #
        # Story
        #

        context = StoryAgent(provider).generate(context)
        self._complete_stage("Story")

        #
        # Scene Plan
        #

        context = SceneAgent(provider).generate(context)
        self._complete_stage("Scene Plan")

        #
        # Image Prompts
        #

        context = ImagePromptAgent(provider).generate(context)
        self._complete_stage("Image Prompts")

        #
        # Narration
        #

        context = NarrationAgent(provider).generate(context)
        self._complete_stage("Narration")

        #
        # Assemble Assets
        #

        assets = AssetAssembler.build(context)
        self._complete_stage("Asset Assembly")

        #
        # Render Media
        #

        rendered = MediaPipeline().render(
            workspace=workspace,
            assets=assets,
        )
        self._complete_stage("Media Rendering")

        #
        # Compose Episode
        #

        scene_videos = [Path(video.video_path) for video in rendered.videos]

        final_episode = EpisodeComposer().compose(
            workspace=workspace,
            scene_videos=scene_videos,
        )

        if rendered.videos:
            rendered.videos[-1].video_path = str(final_episode)

        self._complete_stage("Episode Composition")

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

        result = EpisodeExporter().export(
            workspace=workspace,
            metadata=metadata,
            rendered_episode=rendered,
        )

        self._complete_stage("Export")

        print("=" * 60)
        print("Episode Complete")
        print("=" * 60)
        print(f"Workspace : {result.workspace}")
        print(f"Metadata  : {result.metadata_path}")
        print(f"Video     : {result.video_path}")
        print("=" * 60)

        return result
