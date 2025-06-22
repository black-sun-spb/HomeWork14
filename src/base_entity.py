from abc import ABC, abstractmethod


class BaseEntity(ABC):
    @abstractmethod
    def __str__(self) -> str:
        pass
