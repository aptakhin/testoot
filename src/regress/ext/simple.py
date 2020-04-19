from src.regress.impl.serializer.pickle_serializer import PickleSerializer
from src.regress.impl.storage.local_directory_storage import \
    LocalDirectoryStorage
from src.regress.regress import Regress


class LocalRegress(Regress):
    """The most simple configured Regress"""
    def __init__(self):
        super().__init__(
            storage=LocalDirectoryStorage('.regress'),
            serializer=PickleSerializer(),
        )

    def ensure_exists(self, clear=False):
        return self._storage.ensure_exists(clear=clear)
