"""
Tests for Storage Factory.
"""

from backend.app.storage.local_storage import LocalStorage
from backend.app.storage.storage_factory import StorageFactory


def test_returns_local_storage():

    storage = StorageFactory.storage()

    assert isinstance(
        storage,
        LocalStorage,
    )
