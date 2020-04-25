from regress.impl.run_policy.no_canonize_policy import NoCanonizePolicy
from regress.impl.serializer.pickle_serializer import PickleSerializer
from regress.impl.storage.local_directory_storage import \
    LocalDirectoryStorage
from regress.regress import Regress


class LocalRegress(Regress):
    """The most simple configured Regress. Stores files in .regress folder and
    with pickle serializer"""
    def __init__(self):
        super().__init__(
            storage=LocalDirectoryStorage('.regress'),
            serializer=PickleSerializer(),
            run_policy=NoCanonizePolicy(),
        )

    def ensure_exists(self, clear=False):
        return self._storage.ensure_exists(clear=clear)
