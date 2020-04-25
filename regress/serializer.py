from abc import ABC, abstractmethod

from regress.filetype import FileType


class RegressSerializer(ABC):
    """Abstract serializer for objects canonization"""
    def __init__(self, file_type_hint: FileType):
        self._file_type_hint = file_type_hint

    @abstractmethod
    def load(self, stream):
        pass

    @abstractmethod
    def dump(self, obj, stream):
        pass

    @property
    def file_type_hint(self) -> FileType:
        return self._file_type_hint
