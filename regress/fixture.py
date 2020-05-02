from typing import Optional

from regress.base import RegressContext
from regress.regress import Regress


class RegressFixture:
    """Helper for tests. Stores regress instance and context and bypasses them
    to calls"""
    def __init__(self, regress: Regress, context: RegressContext):
        self._regress = regress
        self._context = context

    def test(self, obj: any, suffix: Optional[str] = None):
        """Test object

        :param obj: test object
        :param suffix: test suffix for making a few regression tests
               in one context
        :return:
        """
        return self._regress.test(obj, context=self._context, suffix=suffix,
                                  comparator=self._context.get_comparator())

    def test_filename(self, filename: str):
        """Test generated file content

        :param filename: test filename
        :return:
        """
        return self._regress.test_filename(
            filename,
            context=self._context,
            comparator=self._context.get_comparator(),
        )
