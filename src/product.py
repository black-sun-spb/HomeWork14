from dataclasses import dataclass
from typing import Dict, List, Optional


@dataclass
class Product:
    name: str
    description: str
    quantity: int
    _price: float = 0.0  # Приватный атрибут

    def __init__(
        self, name: str, description: str, price: float, quantity: int
    ) -> None:
        self.name = name
        self.description = description
        self.quantity = quantity
        self._price = 0.0
        self.price = price  # Использует сеттер

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, value: float) -> None:
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return

        if value < self._price:
            try:
                confirm = (
                    input(
                        f"Цена товара понижается с {self._price} до {value}. Подтвердить? (y/n): "
                    )
                    .strip()
                    .lower()
                )
            except EOFError:
                confirm = (
                    "n"  # На случай если input вызван в тестах или не интерактивно
                )
            if confirm != "y":
                print("Изменение отменено.")
                return

        self._price = value
        print(f"Цена успешно изменена на {self._price}")

    @classmethod
    def new_product(
        cls, product_data: Dict, products_list: Optional[List["Product"]] = None
    ) -> "Product":
        """
        Создаёт объект Product из словаря product_data.
        Если products_list передан, проверяет наличие товара с таким же именем.
        Если найден — объединяет количество и обновляет цену (выбирает большую).
        """
        name = str(product_data["name"])
        description = str(product_data["description"])
        price = float(product_data["price"])
        quantity = int(product_data["quantity"])

        if products_list is not None:
            for prod in products_list:
                if prod.name == name:
                    prod.quantity += quantity
                    if price > prod.price:
                        prod.price = price
                    return prod
            # Если дубликатов нет — создаем и добавляем в список
            new_prod = cls(name, description, price, quantity)
            products_list.append(new_prod)
            return new_prod

        # Если список не передан, просто создаем и возвращаем продукт
        return cls(name, description, price, quantity)

    def __str__(self) -> str:
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."
