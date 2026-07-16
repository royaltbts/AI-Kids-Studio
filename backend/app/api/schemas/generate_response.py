"""
Generate Episode Response Schema.
"""

from pydantic import BaseModel


class GenerateEpisodeResponse(BaseModel):
    """
    Response returned after generating an episode.
    """

    success: bool

    workspace: str

    metadata_path: str

    message: str
