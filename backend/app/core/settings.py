"""
TinyVerse Settings

Centralized application configuration.
"""

from pathlib import Path

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Global application settings.
    """

    model_config = SettingsConfigDict(
        env_file="backend/.env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

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

    AI_PROVIDER: str = Field(
        default="mock",
        description="AI provider to use.",
    )

    OPENAI_API_KEY: str = Field(
        default="",
        description="OpenAI API Key.",
    )

    OPENAI_MODEL: str = Field(
        default="gpt-4.1-mini",
        description="OpenAI model.",
    )

    ANTHROPIC_API_KEY: str = ""

    GEMINI_API_KEY: str = ""


settings = Settings()
