"""
Standalone FFmpeg Video Test
"""

from pathlib import Path

from backend.app.renderers.ffmpeg_video_renderer import FFmpegVideoRenderer


def main() -> None:
    """
    Generate one MP4 using FFmpeg.
    """

    image_path = Path("output/test_image.png")
    audio_path = Path("output/test_audio.mp3")
    output_path = Path("output/test_video.mp4")

    if not image_path.exists():
        raise FileNotFoundError(image_path)

    if not audio_path.exists():
        raise FileNotFoundError(audio_path)

    renderer = FFmpegVideoRenderer()

    result = renderer.render(
        image_path=image_path,
        audio_path=audio_path,
        output_path=output_path,
    )

    print()
    print("=" * 60)
    print("Video generated successfully")
    print("=" * 60)
    print()

    print("Video :", result)


if __name__ == "__main__":
    main()
