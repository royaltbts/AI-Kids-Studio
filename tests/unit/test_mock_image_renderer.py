"""
Unit tests for MockImageRenderer.
"""

from backend.app.core.settings import settings
from backend.app.renderers.mock_image_renderer import MockImageRenderer
from backend.app.schemas.image_prompt import ImagePrompt


def test_render_image():
    """
    Verify that the mock image renderer returns
    a deterministic RenderedImage.
    """

    prompt = ImagePrompt(
        scene_number=1,
        title="Meet Toby",
        prompt="Pixar bear",
        negative_prompt="blurry",
        style="Pixar 3D",
        aspect_ratio="16:9",
    )

    image = MockImageRenderer().render(prompt)

    assert image.scene_number == 1

    assert image.image_path == str(
        settings.OUTPUT_DIR / settings.IMAGE_DIR / "scene_001.png"
    )

    assert image.width == settings.DEFAULT_IMAGE_WIDTH

    assert image.height == settings.DEFAULT_IMAGE_HEIGHT

    assert image.status == "rendered"
