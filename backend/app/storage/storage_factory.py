"""
Storage Factory.
"""

from backend.app.storage.local_storage import LocalStorage


class StorageFactory:
    """
    Creates storage implementations.
    """

    @staticmethod
    def storage():

        return LocalStorage()
