import pytest

from testoot.storages import LocalDirectoryStorage, IoWrapper


def test_root_clear_exception():
    with pytest.raises(ValueError):
        LocalDirectoryStorage('/')


def test_init(tmp_path):
    storage_dir = tmp_path / 'local'
    storage = LocalDirectoryStorage(storage_dir)

    assert storage.root_dir == storage_dir
    assert not storage_dir.exists()
    storage.ensure_exists()
    assert storage_dir.exists()

    storage.ensure_exists()  # Already exists, no error
    assert storage_dir.exists()

    storage.clear_if_exists()  # Clear directory
    assert not storage_dir.exists()


def test_read_and_write(tmp_path):
    storage_dir = tmp_path / 'local'
    storage = LocalDirectoryStorage(storage_dir)
    storage.ensure_exists()

    name = 'test'

    # read empty
    with storage.open_read(name, 'b') as f:
        assert f is None

    f2 = storage.open_read(name, 'b')
    assert isinstance(f2, IoWrapper)
    assert f2._stream is None

    # write
    with storage.open_write(name, 'b') as f:
        f.write(b'abc')

    # read written
    with storage.open_read(name, 'b') as f3:
        assert f3.read() == b'abc'

    f4 = storage.open_read(name, 'b')
    try:
        assert f4.read() == b'abc'
    finally:
        f4.close()


def test_clone(tmp_path):
    storage_dir = tmp_path / 'local'
    storage = LocalDirectoryStorage(storage_dir)

    s1 = storage.clone()
    assert s1.root_dir == storage_dir

    s2 = storage.clone(add_path='add')
    assert s2.root_dir == storage_dir / 'add'
