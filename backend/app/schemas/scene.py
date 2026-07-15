"""
Scene Schema

Represents a single scene in a TinyVerse episode.
"""

from pydantic import BaseModel


class Scene(BaseModel):
    """
    Represents one animated scene.
    """

    scene_number: int

    title: str

    narration: str

    visual_description: str

    duration_seconds: int
