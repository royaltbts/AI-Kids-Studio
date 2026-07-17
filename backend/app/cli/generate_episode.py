"""
TinyVerse CLI

Generate a TinyVerse episode from the command line.
"""

import argparse
import sys

from backend.app.services.episode_workflow import EpisodeWorkflow


def main() -> int:
    """
    CLI entry point.
    """

    parser = argparse.ArgumentParser(
        prog="TinyVerse",
        description="Generate a TinyVerse episode.",
    )

    parser.add_argument(
        "--topic",
        required=True,
        help="Episode topic.",
    )

    parser.add_argument(
        "--age-group",
        required=True,
        help="Target age group.",
    )

    parser.add_argument(
        "--provider",
        choices=[
            "mock",
            "openai",
        ],
        default=None,
        help=("AI provider to use. " "Overrides the value configured in backend/.env."),
    )

    args = parser.parse_args()

    print()
    print("=" * 50)
    print("TinyVerse Kids Studio")
    print("=" * 50)
    print()

    print(f"Topic      : {args.topic}")
    print(f"Age Group  : {args.age_group}")

    if args.provider:
        print(f"Provider   : {args.provider}")

    print()
    print("Generating episode...")
    print()

    workflow = EpisodeWorkflow()

    result = workflow.generate_episode(
        topic=args.topic,
        age_group=args.age_group,
        provider=args.provider,
    )

    print("✓ Episode generated successfully")
    print()

    print(f"Workspace : {result.workspace}")
    print(f"Metadata  : {result.metadata_path}")
    print(f"Success   : {result.success}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
