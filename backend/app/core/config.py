from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    APP_NAME: str = "TinyVerse Kids Studio"

    APP_VERSION: str = "1.0.0"

    OPENAI_API_KEY: str = ""

    AI_PROVIDER: str = "mock"

    model_config = SettingsConfigDict(
        env_file="backend/.env",
        extra="ignore",
    )


settings = Settings()
