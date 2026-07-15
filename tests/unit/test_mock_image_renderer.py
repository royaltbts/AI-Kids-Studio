"""
Unit tests for MockImageRenderer.
"""

from backend.app.renderers.mock_image_renderer import MockImageRenderer
from backend.app.schemas.image_prompt import ImagePrompt


def test_render_image():

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
    assert image.image_path == "renders/scene_001.png"
    assert image.width == 1920
    assert image.height == 1080
    assert image.status == "rendered"
