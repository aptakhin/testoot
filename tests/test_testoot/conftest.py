from typing import Optional

import pytest

from testoot.base import TestootContext, Comparator, TestootSerializer, \
    FileType, TestootTestResult
from testoot.ext.pytest import PytestContext
from testoot.testoot import Testoot
from tests.conftest import AbcDiffResult


@pytest.fixture(scope='module')
def base_testoot(root_base_testoot):
    testoot = root_base_testoot.clone(
        storage=root_base_testoot.storage.clone(add_path='examples'),
    )
    testoot.storage.ensure_exists()
    yield testoot


@pytest.fixture(scope='function')
def testoot(base_testoot, request):
    testoot = Testoot(base_testoot, PytestContext(request))
    yield testoot


class TrueComparator(Comparator):
    @classmethod
    def compare(cls, test_obj: any, canon_obj: any):
        assert True


class FalseComparator(Comparator):
    @classmethod
    def compare(cls, test_obj: any, canon_obj: any):
        assert False


class ContextTestoot(TestootContext):
    def __init__(self, name, comparator: Optional[Comparator] = None,
                 serializer: Optional[TestootSerializer] = None,
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

    def get_serializer(self) -> Optional[TestootSerializer]:
        return self._serializer

    def ask_canonize(self) -> bool:
        return self._ask_canonize

    def create_test_result(self, test_obj: any, canon_obj: any,
                           exc: Exception) -> TestootTestResult:
        return AbcDiffResult()
