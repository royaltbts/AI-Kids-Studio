"""
Tests for Renderer Factory.
"""

from backend.app.renderers.mock_image_renderer import MockImageRenderer
from backend.app.renderers.mock_voice_renderer import MockVoiceRenderer
from backend.app.renderers.renderer_factory import RendererFactory


def test_returns_image_renderer():
    renderer = RendererFactory.image_renderer()

    assert isinstance(
        renderer,
        MockImageRenderer,
    )


def test_returns_voice_renderer():
    renderer = RendererFactory.voice_renderer()

    assert isinstance(
        renderer,
        MockVoiceRenderer,
    )