from typing import Optional

from src.regress.context import RegressContext
from src.regress.regress import Regress


def _make_filename_from_pytest_nodeif(nodeid):
    return (
        nodeid
            .lower()
            .replace('/', '_')
            .replace(':', '_')
            .replace('.', '_')
    )


class PytestContext(RegressContext):
    def __init__(self, request: 'FixtureRequest'):
        self._nodeid = request.node.nodeid

    def get_storage_name(self, suffix: Optional[str]=None):
        name = _make_filename_from_pytest_nodeif(self._nodeid)
        if suffix is not None:
            name += suffix
        return name


class RegressFixture:
    def __init__(self, regress: Regress, request):
        self._regress = regress
        self._context = PytestContext(request)

    def test(self, obj: any, suffix: Optional[str] = None):
        return self._regress.test(obj, context=self._context, suffix=suffix)

    def canonize(self, obj: any, suffix: Optional[str] = None):
        return self._regress.canonize(obj, context=self._context, suffix=suffix)
