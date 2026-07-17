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
        Export metadata and the final episode.
        """

        #
        # Save metadata
        #

        metadata_path = MetadataManager.save(
            workspace,
            metadata,
        )

        #
        # Final composed episode
        #

        video_path = (
            workspace
            / "video"
            / "episode.mp4"
        )

        if not video_path.exists():
            raise FileNotFoundError(
                f"Final episode not found: {video_path}"
            )

        #
        # Export result
        #

        return ExportResult(
            workspace=workspace,
            metadata_path=metadata_path,
            video_path=video_path,
            success=True,
        )