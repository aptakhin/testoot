from abc import ABC, abstractmethod
from io import IOBase

from regress.file_type import FileType


class RegressSerializer(ABC):
    """Abstract serializer for objects canonization"""
    def __init__(self, file_type_hint: FileType):
        """Init

        :param file_type_hint: hint for generating file or resource name
        """
        self._file_type_hint = file_type_hint

    @abstractmethod
    def load(self, stream: IOBase) -> any:
        pass

    @abstractmethod
    def dump(self, obj: any, stream: IOBase):
        pass

    @property
    def file_type_hint(self) -> FileType:
        return self._file_type_hint
