import mimetypes
from abc import ABC, abstractmethod
from dataclasses import dataclass
from io import IOBase
from typing import Optional


class FileTypeNoExtension:
    pass


@dataclass
class FileType:
    """File type hint for tests.

    :param mime: required MIME type
    :param override_file_ext: override default MIME type extension
    """
    mime: str
    override_file_ext: Optional[str] = FileTypeNoExtension

    def get_file_extension(self) -> Optional[str]:
        if self.override_file_ext is not FileTypeNoExtension:
            return self.override_file_ext

        return mimetypes.guess_extension(self.mime, strict=False)


class Comparator(ABC):
    """Abstract type comparator"""
    @abstractmethod
    def compare(self, test_obj: any, canon_obj: any):
        """Compares objects"""
        pass  # pragma: no cover


class TestootTestResult(ABC):
    __test__ = False

    """Abstract test result"""
    @abstractmethod
    def format_diff(self) -> str:
        """Format diff"""
        pass  # pragma: no cover


class TestootSerializer(ABC):
    __test__ = False

    """Abstract serializer for objects canonization"""
    def __init__(self, file_type_hint: FileType, mode: str = 'b'):
        """Init

        :param file_type_hint: hint for generating file or resource name
        :param mode: hint for storage stream
        """
        self._file_type_hint = file_type_hint
        self._mode = mode

    @abstractmethod
    def load(self, stream: IOBase) -> any:
        pass  # pragma: no cover

    @abstractmethod
    def dump(self, obj: any, stream: IOBase):
        pass  # pragma: no cover

    @property
    def file_type_hint(self) -> FileType:
        return self._file_type_hint

    @property
    def mode(self):
        return self._mode


class TestootContext(ABC):
    __test__ = False

    """Abstract test context"""
    @abstractmethod
    def get_storage_name(self, file_type_hint: FileType,
                         suffix: Optional[str] = None):
        """Gets name for test"""
        pass  # pragma: no cover

    @abstractmethod
    def get_storage_name_from_filename(self, filename: str):
        pass  # pragma: no cover

    @abstractmethod
    def get_serializer(self) -> Optional[TestootSerializer]:
        pass  # pragma: no cover

    @abstractmethod
    def get_comparator(self) -> Optional[Comparator]:
        pass  # pragma: no cover

    @abstractmethod
    def ask_canonize(self) -> bool:
        pass  # pragma: no cover

    @abstractmethod
    def create_test_result(self, test_obj: any, canon_obj: any,
                           exc: Exception) -> TestootTestResult:
        pass  # pragma: no cover


class CanonizePolicy(ABC):
    """Abstract run decisions with conflicted tests"""
    @abstractmethod
    def ask_canonize(self, test_result: TestootTestResult) -> bool:
        """Asks user for canonization or decide it by internal tests
        policies"""
        pass  # pragma: no cover


class TestootStorage(ABC):
    __test__ = False

    """Abstract storage for canonized data"""
    @abstractmethod
    def open_read(self, key: str, mode: str) -> Optional[IOBase]:
        pass  # pragma: no cover

    @abstractmethod
    def open_write(self, key: str, mode: str) -> IOBase:
        pass  # pragma: no cover

    @abstractmethod
    def ensure_exists(self):
        pass  # pragma: no cover

    @abstractmethod
    def clear_if_exists(self):
        pass  # pragma: no cover

    @abstractmethod
    def clone(self, *, add_path: Optional[str] = None):
        pass  # pragma: no cover


class UserInteraction(ABC):
    """Abstract interaction with user"""
    @abstractmethod
    def ask_canonize(self, test_result: TestootTestResult) -> bool:
        """Asks user for canonization"""
        pass  # pragma: no cover
