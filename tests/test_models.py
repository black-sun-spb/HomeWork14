import pytest

from src.category import Category
from src.product import Product


@pytest.fixture(autouse=True)
def reset_class_attributes():
    Category.category_count = 0
    Category.product_count = 0


def test_add_product_and_private_products():
    cat = Category("Овощи", "Свежие овощи", [])
    product = Product("Морковь", "Сочная", 50, 10)
    cat.add_product(product)

    assert len(cat._Category__products) == 1
    assert cat._Category__products[0].name == "Морковь"


def test_products_getter_format():
    cat = Category("Фрукты", "Сладкие", [])
    product = Product("Яблоко", "Красное", 80, 15)
    cat.add_product(product)

    formatted = cat.products
    assert formatted == "Яблоко, 80 руб. Остаток: 15 шт."


def test_product_price_validation_negative(capfd):
    product = Product("Тест", "Описание", 100, 1)
    product.price = -10

    out, _ = capfd.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in out
    assert product.price == 100


def test_product_price_validation_zero(capfd):
    product = Product("Тест", "Описание", 100, 1)
    product.price = 0

    out, _ = capfd.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in out
    assert product.price == 100


def test_price_decrease_confirmation(monkeypatch, capfd):
    product = Product("Сыр", "Твёрдый", 150, 2)

    monkeypatch.setattr("builtins.input", lambda _: "n")
    product.price = 100
    out, _ = capfd.readouterr()
    assert "Изменение отменено" in out
    assert product.price == 150

    monkeypatch.setattr("builtins.input", lambda _: "y")
    product.price = 100
    assert product.price == 100


def test_product_str_format():
    p = Product("Банан", "Жёлтый", 60, 7)
    assert str(p) == "Банан, 60 руб. Остаток: 7 шт."


def test_new_product_no_duplicate():
    existing = []
    p = Product.new_product(
        {"name": "Молоко", "description": "1 л", "price": 80, "quantity": 5}, existing
    )

    assert isinstance(p, Product)
    assert len(existing) == 1
    assert existing[0].name == "Молоко"


def test_new_product_merge_duplicate():
    existing = [Product("Молоко", "1 л", 70, 10)]

    p = Product.new_product(
        {"name": "Молоко", "description": "1 л", "price": 90, "quantity": 5}, existing
    )

    assert len(existing) == 1
    assert existing[0].quantity == 15
    assert existing[0].price == 90
    assert p is existing[0]


def test_new_product_without_list():
    p = Product.new_product(
        {"name": "Сок", "description": "Апельсиновый", "price": 90, "quantity": 3}
    )
    assert isinstance(p, Product)
    assert p.name == "Сок"
    assert p.quantity == 3
    assert p.price == 90
