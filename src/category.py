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
        return '\n'.join(
            f"{prod.name}, {prod.price} руб. Остаток: {prod.quantity} шт."
            for prod in self.__products
        )
