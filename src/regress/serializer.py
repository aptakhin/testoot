from abc import ABC, abstractmethod


class RegressSerializer(ABC):
    @abstractmethod
    def load(self, stream):
        pass

    @abstractmethod
    def dump(self, obj, stream):
        pass
