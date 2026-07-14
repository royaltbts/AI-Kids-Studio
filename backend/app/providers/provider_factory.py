from backend.app.providers.mock_provider import MockProvider


class ProviderFactory:

    @staticmethod
    def get_provider():

        return MockProvider()