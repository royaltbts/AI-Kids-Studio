"""
Export Result Schema

Represents the result of exporting an episode.
"""

from pathlib import Path

from pydantic import BaseModel


class ExportResult(BaseModel):
    """
    Result returned after exporting an episode.
    """

    workspace: Path

    metadata_path: Path

    video_path: Path

    success: bool = True
