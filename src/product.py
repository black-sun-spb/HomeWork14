from dataclasses import dataclass


@dataclass
class Product:
    name: str
    description: str
    price: float  # например, 199.99
    quantity: int  # количество в штуках

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity