from typing import Optional

from regress.base import RegressContext, FileType, Comparator


def _make_filename_from_pytest_nodeid(nodeid):
    """Transforms pytest nodeid to safe file name"""
    return (nodeid.lower()
            .replace('/', '_')
            .replace(':', '_')
            .replace('.', '_'))


class PytestComparator(Comparator):
    @classmethod
    def compare(cls, test_obj: any, canon_obj: any):
        """Compares objects"""
        assert test_obj == canon_obj


class PytestContext(RegressContext):
    """Context from Pytest"""
    def __init__(self, request, comparator: Optional[Comparator] = None):
        """Initializes pytest context

        :param request: standard request fixture
        :param comparator: comparison for objects
        """
        self._nodeid = request.node.nodeid
        self._comparator = (PytestComparator() if comparator is None
                            else comparator)

    def get_storage_name(self, file_type_hint: FileType,
                         suffix: Optional[str] = None):
        name = _make_filename_from_pytest_nodeid(self._nodeid)
        if suffix is not None:
            name += suffix

        file_ext = file_type_hint.get_file_extension()
        if file_ext is not None:
            name += file_ext

        return name

    def get_storage_name_from_filename(self, filename: str):
        return filename

    def get_comparator(self) -> Optional[Comparator]:
        return self._comparator
