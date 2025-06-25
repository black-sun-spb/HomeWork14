from typing import Iterator, List

from src.base_entity import BaseEntity
from src.product import Product


class Category(BaseEntity):
    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: List[Product]) -> None:
        self.name = name
        self.description = description
        self.__products: List[Product] = []
        for product in products:
            self.add_product(product)
        Category.category_count += 1

    def add_product(self, product: Product) -> None:
        """Добавить продукт в категорию и увеличить счётчик продуктов"""
        if not isinstance(product, Product):
            raise TypeError(
                "Можно добавлять только объекты класса Product или его наследников"
            )

        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        return "\n".join(str(prod) for prod in self.__products)

    def __str__(self) -> str:
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def __iter__(self) -> Iterator[Product]:
        return CategoryIterator(self)


class CategoryIterator:
    def __init__(self, category: Category) -> None:
        self._products = category._Category__products  # type: ignore[attr-defined]
        self._index = 0

    def __iter__(self) -> "CategoryIterator":
        return self

    def __next__(self) -> Product:
        if self._index >= len(self._products):
            raise StopIteration
        product = self._products[self._index]
        self._index += 1
        return product
