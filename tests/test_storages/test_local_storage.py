import pytest

from regress.impl.storages import LocalDirectoryStorage


def test_root_clear_exception():
    with pytest.raises(ValueError):
        LocalDirectoryStorage('/')
