from abc import ABC, abstractmethod
from typing import Optional

from regress.file_type import FileType


class RegressContext(ABC):
    """Abstract test context"""
    @abstractmethod
    def get_storage_name(self, file_type_hint: FileType,
                         suffix: Optional[str] = None):
        pass
