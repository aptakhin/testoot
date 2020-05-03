from typing import Optional

from regress.base import RegressStorage, RegressSerializer, Comparator, \
    CanonizePolicy
from regress.regress import Regress


class DefaultRegress(Regress):
    """Default configured Regress. Stores files in .regress folder
    with pickle serializer and throws errors on conflict output"""
    def __init__(self, *, storage: Optional[RegressStorage] = None,
                 serializer: Optional[RegressSerializer] = None,
                 canonize_policy: Optional[CanonizePolicy] = None,
                 comparator: Optional[Comparator] = None):
        """Initialize default regress. Every argument is optional and can
        override default behavior.

        :param storage: own storage or :class:`LocalDirectoryStorage`
        :param serializer: own serializer or :class:`PickleSerializer`
        :param canonize_policy: own policy or
               :class:`AskCanonizePolicy` with
               :class:`ConsoleUserInteraction`
        :param comparator: own comparator or use provided by
               :class:`RegressContext`.
        """

        from regress.pub import PickleSerializer, \
            LocalDirectoryStorage, AskCanonizePolicy, \
            ConsoleUserInteraction

        super().__init__(
            storage=storage or LocalDirectoryStorage('.regress'),
            serializer=serializer or PickleSerializer(),
            canonize_policy=(canonize_policy or
                             AskCanonizePolicy(ConsoleUserInteraction())),
            comparator=comparator,
        )

    def ensure_exists(self, clear=False):
        return self._storage.ensure_exists(clear=clear)
