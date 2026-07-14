"""
Scene Asset Schema

Represents all assets required to render a single scene.
"""

from pydantic import BaseModel

from backend.app.schemas.scene import Scene


class SceneAsset(BaseModel):
    """
    Rendering assets for a single scene.
    """

    scene: Scene

    image_prompt: str = ""

    narration: str = ""

    background_music: str = ""

    sound_effects: list[str] = []

    camera_direction: str = ""

    subtitle: str = ""

    animation_notes: str = ""
