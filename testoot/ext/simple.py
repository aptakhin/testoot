from typing import Optional

from testoot.base import TestootStorage, TestootSerializer, Comparator, \
    CanonizePolicy
from testoot.base_testoot import BaseTestoot


class DefaultBaseTestoot(BaseTestoot):
    """Default configured BaseTestoot. Stores files in .testoot folder
    with pickle serializer and throws errors on conflict output"""
    def __init__(self, *, storage: Optional[TestootStorage] = None,
                 serializer: Optional[TestootSerializer] = None,
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
               :class:`TestootContext`.
        """

        from testoot.pub import LocalDirectoryStorage, AskCanonizePolicy, \
            ConsoleUserInteraction
        from testoot.serializers import PickleSerializer

        super().__init__(
            storage=storage or LocalDirectoryStorage('.testoot'),
            serializer=serializer or PickleSerializer(),
            canonize_policy=(canonize_policy or
                             AskCanonizePolicy(ConsoleUserInteraction())),
            comparator=comparator,
        )
