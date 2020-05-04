from typing import Optional

import pytest

from regress.base import RegressContext, Comparator, RegressSerializer, \
    FileType, RegressTestResult
from regress.ext.pytest import PytestContext
from regress.regress import Regress
from tests.conftest import AbcDiffResult


@pytest.fixture(scope='module')
def base_regress(root_base_regress):
    regress = root_base_regress.clone(
        storage=root_base_regress.storage.clone(add_path='examples'),
    )
    regress.storage.ensure_exists()
    yield regress


@pytest.fixture(scope='function')
def regress(base_regress, request):
    regress = Regress(base_regress, PytestContext(request))
    yield regress


class TrueComparator(Comparator):
    @classmethod
    def compare(cls, test_obj: any, canon_obj: any):
        assert True


class FalseComparator(Comparator):
    @classmethod
    def compare(cls, test_obj: any, canon_obj: any):
        assert False


class ContextRegress(RegressContext):
    def __init__(self, name, comparator: Optional[Comparator] = None,
                 serializer: Optional[RegressSerializer] = None,
                 ask_canonize: bool = False):
        self._name = name
        self._comparator = (TrueComparator() if comparator is None
                            else comparator)
        self._serializer = serializer
        self._ask_canonize = ask_canonize

    def get_storage_name(self, file_type_hint: FileType,
                         suffix: Optional[str] = None):
        return self._name

    def get_storage_name_from_filename(self, filename: str):
        return filename

    def get_comparator(self) -> Optional[Comparator]:
        return self._comparator

    def get_serializer(self) -> Optional[RegressSerializer]:
        return self._serializer

    def ask_canonize(self) -> bool:
        return self._ask_canonize

    def create_test_result(self, test_obj: any, canon_obj: any,
                           exc: Exception) -> RegressTestResult:
        return AbcDiffResult()
