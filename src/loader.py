import json
from typing import List

from src.category import Category
from src.product import Product


def load_categories_from_json(file_path: str) -> List[Category]:
    with open(file_path, encoding="utf-8") as f:
        data = json.load(f)

    categories = []
    for cat_data in data:
        products = []
        for prod_data in cat_data.get("products", []):
            product = Product(
                name=prod_data["name"],
                description=prod_data["description"],
                price=float(prod_data["price"]),
                quantity=int(prod_data["quantity"]),
            )
            products.append(product)

        category = Category(
            name=cat_data["name"],
            description=cat_data["description"],
            products=products,
        )
        categories.append(category)

    return categories
