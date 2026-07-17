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
from backend.app.core.settings import settings
from backend.app.schemas.episode_context import EpisodeContext
from backend.app.schemas.episode_metadata import EpisodeMetadata
from backend.app.schemas.export_result import ExportResult
from backend.app.services.asset_assembler import AssetAssembler
from backend.app.services.cost_estimator import CostEstimator
from backend.app.services.episode_composer import EpisodeComposer
from backend.app.services.episode_exporter import EpisodeExporter
from backend.app.services.generation_statistics import (
    GenerationStatisticsService,
)
from backend.app.services.logger_service import LoggerService
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
        Mark a workflow stage as complete.
        """

        self.progress.complete_stage(stage)
        LoggerService.stage_completed(stage)
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

        LoggerService.configure(
            log_file=workspace / "logs" / "episode.log",
        )

        LoggerService.episode_started(
            topic,
            age_group,
        )

        #
        # Statistics
        #

        statistics = GenerationStatisticsService(
            episode_id=workspace.name,
        )

        statistics.set_providers(
            image=settings.IMAGE_PROVIDER,
            voice=settings.VOICE_PROVIDER,
            video=settings.VIDEO_PROVIDER,
        )

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
        # Scene Planning
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

        rendered = MediaPipeline(
            provider=provider,
        ).render(
            workspace=workspace,
            assets=assets,
        )

        statistics.statistics.image_count = len(rendered.images)
        statistics.statistics.audio_count = len(rendered.audio)
        statistics.statistics.video_count = len(rendered.videos)

        self._complete_stage("Media Rendering")

        #
        # Compose Final Episode
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
        # Estimate Cost
        #

        estimated_cost = CostEstimator.estimate_total(
            image_count=len(rendered.images),
            character_count=sum(len(audio.narration) for audio in rendered.audio),
            token_count=0,
        )

        statistics.set_cost(
            estimated_cost,
        )

        #
        # Finalize Statistics
        #

        episode_statistics = statistics.finish()

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
            statistics=episode_statistics,
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

        LoggerService.episode_finished(
            result.workspace,
        )

        #
        # Console Summary
        #

        print("=" * 60)
        print("Episode Complete")
        print("=" * 60)
        print(f"Workspace : {result.workspace}")
        print(f"Metadata  : {result.metadata_path}")
        print(f"Video     : {result.video_path}")
        print()

        print("Generation Statistics")
        print("-" * 60)
        print(f"Elapsed Time : " f"{episode_statistics.elapsed_seconds:.2f} sec")
        print(f"Images       : " f"{episode_statistics.image_count}")
        print(f"Audio        : " f"{episode_statistics.audio_count}")
        print(f"Videos       : " f"{episode_statistics.video_count}")
        print(f"Estimated $  : " f"{episode_statistics.estimated_cost:.4f}")
        print(f"Image Prov.  : " f"{episode_statistics.image_provider}")
        print(f"Voice Prov.  : " f"{episode_statistics.voice_provider}")
        print(f"Video Prov.  : " f"{episode_statistics.video_provider}")
        print("=" * 60)

        return result
