from abc import ABC, abstractmethod
from typing import Optional


class RegressContext(ABC):
    @abstractmethod
    def get_storage_name(self, suffix: Optional[str]=None):
        pass
