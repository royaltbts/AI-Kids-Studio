"""
Unit tests for MockImageRenderer.
"""

from pathlib import Path

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

    output_path = Path("output/images/scene_001.png")

    image = MockImageRenderer().render(
        image_prompt=prompt,
        output_path=output_path,
    )

    assert image.scene_number == 1
    assert image.image_path == str(output_path)
    assert image.width > 0
    assert image.height > 0
    assert image.status == "rendered"
