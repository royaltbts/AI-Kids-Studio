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

    # ==========================================================
    # Application
    # ==========================================================

    PROJECT_NAME: str = "TinyVerse"

    APP_VERSION: str = "1.0.0"

    # ==========================================================
    # Output Directories
    # ==========================================================

    OUTPUT_DIR: Path = Path("output")

    IMAGE_DIR: str = "images"

    AUDIO_DIR: str = "audio"

    MUSIC_DIR: str = "music"

    VIDEO_DIR: str = "video"

    THUMBNAIL_DIR: str = "thumbnails"

    LOG_DIR: str = "logs"

    TRACE_DIR: str = "trace"

    PROMPTS_DIR: str = "prompts"

    RESPONSES_DIR: str = "responses"

    # ==========================================================
    # Rendering Defaults
    # ==========================================================

    DEFAULT_IMAGE_WIDTH: int = 1920

    DEFAULT_IMAGE_HEIGHT: int = 1080

    DEFAULT_FPS: int = 30

    # ==========================================================
    # AI Providers
    # ==========================================================

    AI_PROVIDER: str = Field(
        default="mock",
        description="LLM provider.",
    )

    IMAGE_PROVIDER: str = Field(
        default="mock",
        description="Image provider.",
    )

    VOICE_PROVIDER: str = Field(
        default="mock",
        description="Voice provider.",
    )

    MUSIC_PROVIDER: str = Field(
        default="mock",
        description="Music provider.",
    )

    VIDEO_PROVIDER: str = Field(
        default="mock",
        description="Video provider.",
    )

    # ==========================================================
    # OpenAI
    # ==========================================================

    OPENAI_API_KEY: str = Field(
        default="",
        description="OpenAI API Key.",
    )

    OPENAI_MODEL: str = Field(
        default="gpt-4.1-mini",
        description="OpenAI LLM model.",
    )

    OPENAI_IMAGE_MODEL: str = Field(
        default="gpt-image-1",
        description="OpenAI Image model.",
    )

    OPENAI_TTS_MODEL: str = Field(
        default="gpt-4o-mini-tts",
        description="OpenAI TTS model.",
    )

    OPENAI_TTS_VOICE: str = Field(
        default="alloy",
        description="OpenAI voice.",
    )

    # ==========================================================
    # Future Providers
    # ==========================================================

    ANTHROPIC_API_KEY: str = ""

    GEMINI_API_KEY: str = ""


settings = Settings()
