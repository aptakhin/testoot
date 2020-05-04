from typing import Optional

from regress.base import RegressContext, Comparator, RegressSerializer
from regress.regress import Regress


class RegressFixture:
    """Helper for tests. Stores regress instance and context and bypasses them
    to calls"""
    def __init__(self, regress: Regress, context: RegressContext):
        self._regress = regress
        self._context = context

    def test(self, obj: any, suffix: Optional[str] = None,
             comparator: Optional[Comparator] = None,
             serializer: Optional[RegressSerializer] = None,
             ):
        """Test object

        :param obj: test object
        :param suffix: test suffix for making a few regression tests
               in one context
        :param comparator: custom comparator override
        :param serializer: custom serializer override
        :return:
        """
        return self._regress.test(obj, context=self._context, suffix=suffix,
                                  comparator=comparator, serializer=serializer)

    def test_filename(self, filename: str,
                      comparator: Optional[Comparator] = None,
                      serializer: Optional[RegressSerializer] = None,
                      ):
        """Test generated file content

        :param filename: test filename
        :param comparator: custom comparator override
        :param serializer: custom serializer override
        :return:
        """
        return self._regress.test_filename(
            filename,
            context=self._context,
            comparator=comparator,
            serializer=serializer,
        )
