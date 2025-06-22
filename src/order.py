from src.base_entity import BaseEntity
from src.product import Product


class Order(BaseEntity):
    def __init__(self, product: Product, quantity: int) -> None:
        self.product = product
        self.quantity = quantity
        self.total_price = self.product.price * quantity

    def __str__(self) -> str:
        return (
            f"Заказ: {self.product.name} x {self.quantity} шт. = "
            f"{self.total_price} руб."
        )
