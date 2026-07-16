"""
Metadata Manager

Handles reading and writing episode metadata.
"""

from pathlib import Path

from backend.app.schemas.episode_metadata import EpisodeMetadata


class MetadataManager:
    """
    Reads and writes episode metadata.
    """

    METADATA_FILE = "metadata.json"

    @classmethod
    def save(
        cls,
        workspace: Path,
        metadata: EpisodeMetadata,
    ) -> Path:
        """
        Save metadata to the episode workspace.
        """

        metadata_path = workspace / cls.METADATA_FILE

        metadata_path.write_text(
            metadata.model_dump_json(
                indent=4,
            ),
            encoding="utf-8",
        )

        return metadata_path

    @classmethod
    def load(
        cls,
        workspace: Path,
    ) -> EpisodeMetadata:
        """
        Load metadata from the episode workspace.
        """

        metadata_path = workspace / cls.METADATA_FILE

        return EpisodeMetadata.model_validate_json(
            metadata_path.read_text(
                encoding="utf-8",
            )
        )

    @classmethod
    def exists(
        cls,
        workspace: Path,
    ) -> bool:
        """
        Check whether metadata exists.
        """

        return (workspace / cls.METADATA_FILE).exists()
