"""
Standalone Episode Composer Test

Finds the latest episode workspace and composes all scene videos
into one episode.mp4.
"""

from pathlib import Path

from backend.app.core.settings import settings
from backend.app.services.episode_composer import EpisodeComposer


def latest_workspace() -> Path:
    """
    Return the most recently created episode workspace.
    """

    output_dir = settings.OUTPUT_DIR

    workspaces = sorted(
        [
            path
            for path in output_dir.iterdir()
            if path.is_dir() and path.name.startswith("episode_")
        ]
    )

    if not workspaces:
        raise FileNotFoundError("No episode workspaces were found.")

    return workspaces[-1]


def main() -> None:
    """
    Compose the latest rendered episode.
    """

    workspace = latest_workspace()

    video_dir = workspace / settings.VIDEO_DIR

    scene_videos = sorted(video_dir.glob("scene_*.mp4"))

    if not scene_videos:
        raise FileNotFoundError(f"No scene videos found in {video_dir}")

    composer = EpisodeComposer()

    episode_video = composer.compose(
        workspace=workspace,
        scene_videos=scene_videos,
    )

    print()
    print("=" * 60)
    print("Episode composed successfully")
    print("=" * 60)
    print()

    print("Workspace :", workspace)
    print("Scenes    :", len(scene_videos))
    print("Episode   :", episode_video)


if __name__ == "__main__":
    main()
