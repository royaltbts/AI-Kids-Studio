"""
Local filesystem storage.
"""

from pathlib import Path

from backend.app.storage.base_storage import BaseStorage


class LocalStorage(BaseStorage):
    """
    Stores rendered assets locally.
    """

    BASE_DIR = Path("output")

    def save(
        self,
        relative_path: str,
        content: bytes,
    ) -> Path:

        destination = self.BASE_DIR / relative_path

        destination.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        destination.write_bytes(content)

        return destination

    def exists(
        self,
        relative_path: str,
    ) -> bool:

        return (self.BASE_DIR / relative_path).exists()
