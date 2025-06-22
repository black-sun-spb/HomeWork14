import json
import os
import tempfile

from src.loader import load_categories_from_json


def test_load_categories_from_json():
    test_data = [
        {
            "name": "Смартфоны",
            "description": "Телефоны разных марок",
            "products": [
                {
                    "name": "iPhone",
                    "description": "Pro Max",
                    "price": 150000,
                    "quantity": 5,
                },
                {
                    "name": "Samsung",
                    "description": "Galaxy S",
                    "price": 120000,
                    "quantity": 3,
                },
            ],
        }
    ]

    # Создаём временный файл с JSON
    with tempfile.NamedTemporaryFile(
        delete=False, suffix=".json", mode="w", encoding="utf-8"
    ) as tmp:
        json.dump(test_data, tmp, ensure_ascii=False)
        tmp_path = tmp.name

    try:
        categories = load_categories_from_json(tmp_path)

        assert len(categories) == 1
        category = categories[0]
        assert category.name == "Смартфоны"
        assert category.description == "Телефоны разных марок"
        assert "iPhone" in category.products
        assert "Samsung" in category.products

    finally:
        os.remove(tmp_path)
