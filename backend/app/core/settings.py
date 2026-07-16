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
    # Rendering
    # ==========================================================

    DEFAULT_IMAGE_WIDTH: int = 1920

    DEFAULT_IMAGE_HEIGHT: int = 1080

    DEFAULT_FPS: int = 30

    # ==========================================================
    # AI Providers
    # ==========================================================

    AI_PROVIDER: str = Field(
        default="mock",
        description="LLM provider used by AI agents.",
    )

    OPENAI_API_KEY: str = Field(
        default="",
        description="OpenAI API key.",
    )

    OPENAI_MODEL: str = Field(
        default="gpt-4.1-mini",
        description="OpenAI chat model.",
    )

    ANTHROPIC_API_KEY: str = ""

    GEMINI_API_KEY: str = ""

    # ==========================================================
    # Media Renderers
    # ==========================================================

    IMAGE_PROVIDER: str = Field(
        default="mock",
        description="Image renderer implementation.",
    )

    VOICE_PROVIDER: str = Field(
        default="mock",
        description="Voice renderer implementation.",
    )

    MUSIC_PROVIDER: str = Field(
        default="mock",
        description="Music renderer implementation.",
    )

    VIDEO_PROVIDER: str = Field(
        default="mock",
        description="Video renderer implementation.",
    )

    # ==========================================================
    # OpenAI Images
    # ==========================================================

    OPENAI_IMAGE_MODEL: str = Field(
        default="gpt-image-1",
        description="OpenAI image generation model.",
    )

    # ==========================================================
    # OpenAI TTS
    # ==========================================================

    OPENAI_TTS_MODEL: str = Field(
        default="gpt-4o-mini-tts",
        description="OpenAI text-to-speech model.",
    )

    OPENAI_TTS_VOICE: str = Field(
        default="alloy",
        description="Default OpenAI voice.",
    )


settings = Settings()
