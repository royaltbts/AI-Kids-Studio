"""
Tests for OpenAIProvider.
"""

from backend.app.providers.openai_provider import OpenAIProvider


def test_provider_name():
    """
    Verify provider name.
    """

    provider = OpenAIProvider()

    assert provider.provider_name() == "openai"
