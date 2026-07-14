"""
Unit tests for ProviderFactory.
"""

from backend.app.providers.mock_provider import MockProvider
from backend.app.providers.provider_factory import ProviderFactory


def test_returns_mock_provider():
    provider = ProviderFactory.get_provider()

    assert isinstance(provider, MockProvider)