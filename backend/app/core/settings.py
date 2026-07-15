"""
TinyVerse Settings

Centralized application configuration.
"""

from pathlib import Path

from pydantic import BaseModel


class Settings(BaseModel):
    """
    Global application settings.
    """

    PROJECT_NAME: str = "TinyVerse"

    OUTPUT_DIR: Path = Path("output")

    IMAGE_DIR: str = "images"

    AUDIO_DIR: str = "audio"

    MUSIC_DIR: str = "music"

    VIDEO_DIR: str = "video"

    THUMBNAIL_DIR: str = "thumbnails"

    LOG_DIR: str = "logs"

    DEFAULT_IMAGE_WIDTH: int = 1920

    DEFAULT_IMAGE_HEIGHT: int = 1080

    DEFAULT_FPS: int = 30


settings = Settings()
