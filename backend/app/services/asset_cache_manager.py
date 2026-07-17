"""
Asset Cache Manager

Provides helper methods to determine whether rendered assets
already exist and can be reused.
"""

from pathlib import Path


class AssetCacheManager:
    """
    Utility class for checking cached media assets.
    """

    @staticmethod
    def exists(path: Path) -> bool:
        """
        Return True if an asset already exists.

        Parameters
        ----------
        path : Path
            Path to the asset.

        Returns
        -------
        bool
            True if the file exists.
        """

        return path.exists()

    @staticmethod
    def ensure_directory(path: Path) -> None:
        """
        Ensure the parent directory exists.

        Parameters
        ----------
        path : Path
            Asset path.
        """

        path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

    @staticmethod
    def should_render(path: Path) -> bool:
        """
        Determine whether an asset needs rendering.

        Parameters
        ----------
        path : Path
            Output asset path.

        Returns
        -------
        bool
            True when rendering should proceed.
        """

        return not AssetCacheManager.exists(path)
