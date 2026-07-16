"""
Standalone OpenAI Image Renderer Test
"""

from pathlib import Path

from backend.app.renderers.openai_image_renderer import OpenAIImageRenderer
from backend.app.schemas.image_prompt import ImagePrompt


def main() -> None:
    """
    Generate one image using the OpenAI image renderer.
    """

    prompt = ImagePrompt(
        scene_number=1,
        title="Friendly Dinosaur",
        prompt=(
            "A cute green baby dinosaur smiling in a colorful prehistoric "
            "forest, Pixar-style 3D animation, vibrant colors, friendly for "
            "children aged 3-7, cinematic lighting, highly detailed."
        ),
        negative_prompt="blurry, scary, dark, horror",
        style="Pixar 3D",
        aspect_ratio="16:9",
    )

    output_path = Path("output/test_image.png")

    renderer = OpenAIImageRenderer()

    result = renderer.render(
        image_prompt=prompt,
        output_path=output_path,
    )

    print()
    print("=" * 50)
    print("Image generated successfully")
    print("=" * 50)
    print()

    print("Scene :", result.scene_number)
    print("Image :", result.image_path)
    print("Width :", result.width)
    print("Height:", result.height)
    print("Status:", result.status)


if __name__ == "__main__":
    main()
