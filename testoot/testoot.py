from typing import Optional

from testoot.base import TestootContext, Comparator, TestootSerializer, \
    TestootStorage, CanonizePolicy
from testoot.base_testoot import BaseTestoot


class Testoot:
    __test__ = False  # Disable pytest collection warning

    """Main class. Stores base Testoot instance and context and
    bypasses them to calls"""
    def __init__(self, base: BaseTestoot, context: TestootContext):
        self._base = base
        self._context = context

    def test(self, obj: any, suffix: Optional[str] = None,
             comparator: Optional[Comparator] = None,
             serializer: Optional[TestootSerializer] = None,
             ):
        """Tests object.

        :param obj: test object
        :param suffix: test suffix for making a few tests
               in one context
        :param comparator: custom comparator override
        :param serializer: custom serializer override
        :return:
        """
        return self._base.test(
            obj,
            context=self._context,
            suffix=suffix,
            comparator=comparator,
            serializer=serializer,
        )

    def test_filename(self, filename: str,
                      comparator: Optional[Comparator] = None,
                      serializer: Optional[TestootSerializer] = None,
                      ):
        """Tests generated file content.

        :param filename: test filename
        :param comparator: custom comparator override
        :param serializer: custom serializer override
        :return:
        """
        return self._base.test_filename(
            filename,
            context=self._context,
            comparator=comparator,
            serializer=serializer,
        )

    @property
    def base(self) -> BaseTestoot:
        return self._base

    @property
    def storage(self) -> TestootStorage:
        return self._base.storage

    @property
    def canonize_policy(self) -> CanonizePolicy:
        return self._base.canonize_policy
