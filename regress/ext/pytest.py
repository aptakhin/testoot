from typing import Optional

from regress.context import RegressContext
from regress.filetype import FileType


def _make_filename_from_pytest_nodeid(nodeid):
    """Transforms pytest nodeid to safe file name"""
    return (nodeid.lower()
            .replace('/', '_')
            .replace(':', '_')
            .replace('.', '_'))


class PytestContext(RegressContext):
    """Context from Pytest"""
    def __init__(self, request):
        self._nodeid = request.node.nodeid

    def get_storage_name(self, file_type_hint: FileType,
                         suffix: Optional[str] = None):
        name = _make_filename_from_pytest_nodeid(self._nodeid)
        if suffix is not None:
            name += suffix

        file_ext = file_type_hint.get_file_extension()
        if file_ext is not None:
            name += file_ext

        return name
