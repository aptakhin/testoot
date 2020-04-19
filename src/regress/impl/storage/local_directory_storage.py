import shutil
from io import IOBase
from pathlib import Path
from typing import Optional

from src.regress.storage import RegressStorage


class IoWrapper:
    def __init__(self, stream: Optional[IOBase]):
        self._stream = stream

    def __enter__(self):
        return self._stream.__enter__() if self._stream is not None else None

    def __exit__(self, exc_type, exc_val, exc_tb):
        return self._stream.__exit__(exc_type, exc_val, exc_tb) \
            if self._stream is not None else None


class LocalDirectoryStorage(RegressStorage):
    def __init__(self, root_dir):
        self._root_dir = Path(root_dir)

    def open_read(self, key: str) -> Optional[IOBase]:
        path = self._get_path(key)
        if not path.exists():
            return IoWrapper(None)

        return open(self._get_path(key), "rb")

    def open_write(self, key: str) -> IOBase:
        path = self._get_path(key)
        return open(path, "wb")

    def ensure_exists(self, clear=False):
        """ Ensure local directory exists

        :param clear: remove whole folder if exists
        :return:
        """
        if clear and self._root_dir.exists():
            if self._root_dir == '/':
                raise ValueError("Please not remove root!")
            shutil.rmtree(self._root_dir)

        self._root_dir.mkdir(parents=True, exist_ok=True)

    def _get_path(self, key: str):
        return self._root_dir / key
