import pytest

from regress.storages import LocalDirectoryStorage


def test_root_clear_exception():
    with pytest.raises(ValueError):
        LocalDirectoryStorage('/')
