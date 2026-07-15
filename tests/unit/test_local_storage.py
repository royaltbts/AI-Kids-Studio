"""
Tests for Local Storage.
"""

from backend.app.storage.local_storage import LocalStorage


def test_save_file(tmp_path):

    storage = LocalStorage()

    storage.BASE_DIR = tmp_path

    path = storage.save(
        "images/test.txt",
        b"Hello TinyVerse",
    )

    assert path.exists()

    assert path.read_text() == "Hello TinyVerse"

    assert storage.exists(
        "images/test.txt",
    )
