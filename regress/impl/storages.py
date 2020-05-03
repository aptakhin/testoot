import shutil
from io import IOBase, TextIOWrapper
from pathlib import Path
from typing import Optional

from regress.base import RegressStorage


class IoWrapper:
    def __init__(self, stream: Optional[IOBase]):
        self._stream = stream

    def __enter__(self):
        return self._stream.__enter__() if self._stream is not None else None

    def __exit__(self, exc_type, exc_val, exc_tb):
        return self._stream.__exit__(exc_type, exc_val, exc_tb) \
            if self._stream is not None else None


class LocalDirectoryStorage(RegressStorage):
    """Local directory storage"""
    def __init__(self, root_dir):
        self._root_dir = Path(root_dir)
        if self._root_dir == self._root_dir.parent:
            raise ValueError('Root local storage is not supported due '
                             'to safety reasons!')

    def open_read(self, key: str, mode: str) -> Optional[IOBase]:
        path = self._get_path(key)
        if not path.exists():
            return IoWrapper(None)

        stream = open(self._get_path(key), 'rb')
        stream = TextIOWrapper(stream) if mode == 't' else stream
        return stream

    def open_write(self, key: str, mode: str) -> IOBase:
        path = self._get_path(key)
        stream = open(path, 'wb')
        stream = TextIOWrapper(stream) if mode == 't' else stream
        return stream

    def ensure_exists(self, clear=False):
        """Ensure local directory exists

        :param clear: remove whole folder if exists
        :return:
        """
        if clear and self._root_dir.exists():
            shutil.rmtree(self._root_dir)

        self._root_dir.mkdir(parents=True, exist_ok=True)

    def _get_path(self, key: str):
        return self._root_dir / key
