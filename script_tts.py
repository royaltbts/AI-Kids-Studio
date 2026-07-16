"""
Standalone OpenAI TTS Test
"""

from pathlib import Path

from backend.app.renderers.openai_voice_renderer import OpenAIVoiceRenderer
from backend.app.schemas.narration import Narration


def main() -> None:
    """
    Generate one narration using OpenAI TTS.
    """

    narration = Narration(
        scene_number=1,
        title="Welcome",
        narration=(
            "Hello, friends! Welcome to TinyVerse. Today we are going to "
            "learn about friendly dinosaurs. Let's begin our adventure!"
        ),
        voice="alloy",
        duration_seconds=10,
    )

    output_path = Path("output/test_audio.mp3")

    renderer = OpenAIVoiceRenderer()

    result = renderer.render(
        narration=narration,
        output_path=output_path,
    )

    print()
    print("=" * 50)
    print("Audio generated successfully")
    print("=" * 50)
    print()

    print("Scene   :", result.scene_number)
    print("Title   :", result.title)
    print("Audio   :", result.audio_path)
    print("Provider:", result.provider)
    print("Status  :", result.status)


if __name__ == "__main__":
    main()
