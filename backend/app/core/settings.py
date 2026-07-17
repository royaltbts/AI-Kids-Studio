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
        description="OpenAI API Key.",
    )

    OPENAI_MODEL: str = Field(
        default="gpt-4.1-mini",
        description="OpenAI Chat Model.",
    )

    ANTHROPIC_API_KEY: str = ""
    GEMINI_API_KEY: str = ""

    # ==========================================================
    # Image Providers
    # ==========================================================

    IMAGE_PROVIDER: str = Field(
        default="mock",
        description="Image provider implementation.",
    )

    OPENAI_IMAGE_MODEL: str = Field(
        default="gpt-image-1",
        description="OpenAI Image Model.",
    )

    # ==========================================================
    # Voice Providers
    # ==========================================================

    VOICE_PROVIDER: str = Field(
        default="mock",
        description="Voice provider implementation.",
    )

    OPENAI_TTS_MODEL: str = Field(
        default="gpt-4o-mini-tts",
        description="OpenAI TTS Model.",
    )

    OPENAI_TTS_VOICE: str = Field(
        default="alloy",
        description="OpenAI Voice.",
    )

    # ==========================================================
    # Music Providers
    # ==========================================================

    MUSIC_PROVIDER: str = Field(
        default="mock",
        description="Music provider implementation.",
    )

    # ==========================================================
    # Video Providers
    # ==========================================================

    VIDEO_PROVIDER: str = Field(
        default="mock",
        description="Video provider implementation.",
    )

    # ==========================================================
    # Retry Configuration
    # ==========================================================

    OPENAI_MAX_RETRIES: int = Field(
        default=3,
        description="Maximum number of retries for transient OpenAI API failures.",
    )

    OPENAI_RETRY_DELAY: float = Field(
        default=1.0,
        description="Initial retry delay in seconds.",
    )

    OPENAI_RETRY_BACKOFF: float = Field(
        default=2.0,
        description="Exponential backoff multiplier.",
    )

    # ==========================================================
    # Cost Estimation
    # ==========================================================

    OPENAI_IMAGE_COST: float = Field(
        default=0.04,
        description="Estimated cost per generated image in USD.",
    )

    OPENAI_TTS_COST_PER_1K: float = Field(
        default=0.015,
        description="Estimated TTS cost per 1,000 characters in USD.",
    )

    OPENAI_LLM_COST_PER_1K: float = Field(
        default=0.005,
        description="Estimated LLM cost per 1,000 tokens in USD.",
    )


settings = Settings()
