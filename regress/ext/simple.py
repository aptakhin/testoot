from regress.pub import NoCanonizePolicy, PickleSerializer, \
    LocalDirectoryStorage, Regress


class LocalRegress(Regress):
    """The most simple configured Regress. Stores files in .regress folder
    with pickle serializer and throws errors on conflict output"""
    def __init__(self):
        super().__init__(
            storage=LocalDirectoryStorage('.regress'),
            serializer=PickleSerializer(),
            canonize_policy=NoCanonizePolicy(),
        )

    def ensure_exists(self, clear=False):
        return self._storage.ensure_exists(clear=clear)
