"""
Generate Episode Request Schema.
"""

from pydantic import BaseModel, Field


class GenerateEpisodeRequest(BaseModel):
    """
    Request body for generating a TinyVerse episode.
    """

    topic: str = Field(
        ...,
        min_length=1,
        max_length=100,
        description="Episode topic.",
        examples=["ABC"],
    )

    age_group: str = Field(
        ...,
        min_length=3,
        max_length=20,
        description="Target age group.",
        examples=["3-5"],
    )
