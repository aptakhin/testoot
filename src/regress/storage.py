from abc import ABC, abstractmethod
from io import IOBase
from typing import Optional


class RegressStorage(ABC):
    @abstractmethod
    def open_read(self, key: str) -> Optional[IOBase]:
        pass

    @abstractmethod
    def open_write(self, key: str) -> IOBase:
        pass
