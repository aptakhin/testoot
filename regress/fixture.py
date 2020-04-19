from typing import Optional

from regress.context import RegressContext
from regress.regress import Regress


class RegressFixture:
    """Helper for tests. Stores regress instance link and context"""
    def __init__(self, regress: Regress, context: RegressContext):
        self._regress = regress
        self._context = context

    def test(self, obj: any, suffix: Optional[str] = None):
        return self._regress.test(obj, context=self._context, suffix=suffix)

    def canonize(self, obj: any, suffix: Optional[str] = None):
        return self._regress.canonize(obj, context=self._context,
                                      suffix=suffix)
