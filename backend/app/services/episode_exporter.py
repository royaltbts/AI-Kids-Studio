"""
Episode Exporter

Exports a fully rendered episode to an episode workspace.
"""

from pathlib import Path

from backend.app.schemas.episode_metadata import EpisodeMetadata
from backend.app.schemas.export_result import ExportResult
from backend.app.schemas.rendered_episode import RenderedEpisode
from backend.app.services.metadata_manager import MetadataManager


class EpisodeExporter:
    """
    Exports a rendered episode.
    """

    def export(
        self,
        workspace: Path,
        metadata: EpisodeMetadata,
        rendered_episode: RenderedEpisode,
    ) -> ExportResult:
        """
        Export a rendered episode.

        The workspace is created earlier by EpisodeWorkflow and passed
        into the exporter.
        """

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
