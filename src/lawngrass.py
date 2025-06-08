# src/lawngrass.py

from src.product import Product


class LawnGrass(Product):
    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ) -> None:
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __str__(self) -> str:
        base = super().__str__()
        return f"{base}\n{self.country}, цвет: {self.color}, срок прорастания: {self.germination_period}"
