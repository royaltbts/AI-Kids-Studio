"""
Unit tests for ProviderFactory.
"""

from backend.app.providers.mock_provider import MockProvider
from backend.app.providers.provider_factory import ProviderFactory


def test_returns_mock_provider():
    """
    Verify that requesting the mock provider returns MockProvider.
    """

    provider = ProviderFactory.get_provider("mock")

    assert isinstance(provider, MockProvider)
