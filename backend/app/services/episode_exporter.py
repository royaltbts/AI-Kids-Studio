"""
Episode Exporter

Exports a fully rendered episode to an episode workspace.
"""

from pathlib import Path

from backend.app.schemas.episode_metadata import EpisodeMetadata
from backend.app.schemas.export_result import ExportResult
from backend.app.schemas.rendered_episode import RenderedEpisode
from backend.app.services.metadata_manager import MetadataManager
from backend.app.storage.output_manager import OutputManager


class EpisodeExporter:
    """
    Exports a rendered episode.
    """

    def export(
        self,
        metadata: EpisodeMetadata,
        rendered_episode: RenderedEpisode,
    ) -> ExportResult:
        """
        Export a rendered episode.
        """

        workspace = OutputManager.create_episode_workspace()

        metadata_path = MetadataManager.save(
            workspace,
            metadata,
        )

        video_path = (
            Path(rendered_episode.video.video_path)
            if rendered_episode.video
            else Path()
        )

        return ExportResult(
            workspace=workspace,
            metadata_path=metadata_path,
            video_path=video_path,
            success=True,
        )
