"""
Tests for RendererFactory.
"""

from backend.app.core.settings import settings
from backend.app.renderers.mock_image_renderer import MockImageRenderer
from backend.app.renderers.mock_voice_renderer import MockVoiceRenderer
from backend.app.renderers.openai_image_renderer import OpenAIImageRenderer
from backend.app.renderers.openai_voice_renderer import OpenAIVoiceRenderer
from backend.app.renderers.renderer_factory import RendererFactory


def test_returns_image_renderer():
    """
    Verify the configured image renderer is returned.
    """

    renderer = RendererFactory.image_renderer()

    if settings.IMAGE_PROVIDER == "mock":
        assert isinstance(renderer, MockImageRenderer)
    else:
        assert isinstance(renderer, OpenAIImageRenderer)


def test_returns_voice_renderer():
    """
    Verify the configured voice renderer is returned.
    """

    renderer = RendererFactory.voice_renderer()

    if settings.VOICE_PROVIDER == "mock":
        assert isinstance(renderer, MockVoiceRenderer)
    else:
        assert isinstance(renderer, OpenAIVoiceRenderer)
