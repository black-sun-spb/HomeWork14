from typing import List

from src.product import Product


class Category:
    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: List[Product]) -> None:
        self.name = name
        self.description = description
        self.__products: List[Product] = []  # приватный список
        for product in products:
            self.add_product(product)  # учёт добавления через метод

        Category.category_count += 1

    def add_product(self, product: Product) -> None:
        """Добавить продукт в категорию и увеличить счётчик продуктов"""
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        """Вернуть список продуктов в виде форматированных строк, каждый с новой строки"""
        return "".join(
            f"{p.name}, {p.price} руб. Остаток: {p.quantity} шт.\n"
            for p in self.__products
        )
