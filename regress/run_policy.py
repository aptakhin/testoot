from abc import ABC, abstractmethod

from regress.context import RegressContext


class RunPolicy(ABC):
    @abstractmethod
    def ask_canonize(self, context: RegressContext, exc: Exception) -> bool:
        """Asks user for canonization or decide it by internal tests
        policies"""
        pass
