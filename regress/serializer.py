from abc import ABC, abstractmethod


class RegressSerializer(ABC):
    """Abstract serializer for objects canonization"""
    @abstractmethod
    def load(self, stream):
        pass

    @abstractmethod
    def dump(self, obj, stream):
        pass
