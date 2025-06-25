from src.base_entity import BaseEntity
from src.exceptions import ZeroQuantityError
from src.product import Product


class Order(BaseEntity):
    def __init__(self, product: Product, quantity: int) -> None:
        try:
            if quantity <= 0:
                raise ZeroQuantityError()
            self.product = product
            self.quantity = quantity
            self.total_price = product.price * quantity
        except ZeroQuantityError as e:
            print(f"Ошибка: {e}")
            raise
        else:
            print(f"Заказ на товар '{product.name}' успешно создан.")
        finally:
            print("Обработка создания заказа завершена.")

    def __str__(self) -> str:
        return (
            f"Заказ: {self.product.name} x {self.quantity} шт. = "
            f"{self.total_price} руб."
        )
