from typing import Optional

from regress.base import RegressContext, Comparator, RegressSerializer, \
    RegressStorage, CanonizePolicy
from regress.base_regress import BaseRegress


class Regress:
    """Regress main class. Stores base regress instance and context and
    bypasses them to calls"""
    def __init__(self, base: BaseRegress, context: RegressContext):
        self._base = base
        self._context = context

    def test(self, obj: any, suffix: Optional[str] = None,
             comparator: Optional[Comparator] = None,
             serializer: Optional[RegressSerializer] = None,
             ):
        """Test object.

        :param obj: test object
        :param suffix: test suffix for making a few regression tests
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
                      serializer: Optional[RegressSerializer] = None,
                      ):
        """Test generated file content.

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
    def base(self) -> BaseRegress:
        return self._base

    @property
    def storage(self) -> RegressStorage:
        return self._base.storage

    @property
    def canonize_policy(self) -> CanonizePolicy:
        return self._base.canonize_policy
