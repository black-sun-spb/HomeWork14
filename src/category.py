from dataclasses import dataclass, field
from typing import List
from product import Product


@dataclass
class Category:
    name: str
    description: str
    products: List[Product] = field(default_factory=list)

    # 🔵 Атрибуты класса (общие для всех объектов)
    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: List[Product]) -> None:
        self.name = name
        self.description = description
        self.products = products

        # 🔄 Увеличиваем счётчики
        Category.category_count += 1
        Category.product_count += len(products)
