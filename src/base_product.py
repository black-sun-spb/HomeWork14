from abc import ABC, abstractmethod


class BaseProduct(ABC):
    @abstractmethod
    def __init__(
        self, name: str, description: str, price: float, quantity: int
    ) -> None:
        self.name = name
        self.description = description
        self.quantity = quantity
        self.price = price  # Через сеттер

    @property
    @abstractmethod
    def price(self) -> float:
        pass

    @price.setter
    @abstractmethod
    def price(self, value: float) -> None:
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass
