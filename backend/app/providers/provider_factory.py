
from backend.app.core.config import settings
from backend.app.providers.mock_provider import MockProvider


class ProviderFactory:

    @staticmethod
    def get_provider():

        provider = settings.AI_PROVIDER.lower()

        if provider == "mock":
            return MockProvider()

        # We'll add Claude here next
        # We'll add Gemini here next
        # We'll add OpenAI here later

        return MockProvider()