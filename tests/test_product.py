import pytest

from src.exceptions import ZeroQuantityError
from src.lawngrass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone


def test_product_str_format():
    p = Product("Банан", "Жёлтый", 60, 7)
    assert str(p) == "Банан, 60 руб. Остаток: 7 шт."


def test_price_setter_validation_zero(capfd):
    p = Product("Тест", "Описание", 100, 1)
    p.price = 0
    out, _ = capfd.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in out
    assert p.price == 100


def test_price_setter_validation_negative(capfd):
    p = Product("Тест", "Описание", 100, 1)
    p.price = -10
    out, _ = capfd.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in out
    assert p.price == 100


def test_price_decrease_confirmation(monkeypatch, capfd):
    p = Product("Сыр", "Твёрдый", 150, 2)

    # отказ от изменения
    monkeypatch.setattr("builtins.input", lambda _: "n")
    p.price = 100
    out, _ = capfd.readouterr()
    assert "Изменение отменено" in out
    assert p.price == 150

    # подтверждение изменения
    monkeypatch.setattr("builtins.input", lambda _: "y")
    p.price = 100
    assert p.price == 100


def test_product_addition_same_class():
    a = Product("A", "desc", 100, 10)
    b = Product("B", "desc", 200, 2)
    assert a + b == 100 * 10 + 200 * 2


def test_product_addition_different_classes():
    a = Smartphone("Phone A", "desc", 100, 10, "X", "256", "Z", "black")
    b = LawnGrass("Трава", "desc", 200, 2, "Россия", "5 дней", "зелёный")
    with pytest.raises(TypeError, match="Складывать можно только товары одного типа"):
        _ = a + b


def test_new_product_without_list():
    p = Product.new_product(
        {"name": "Молоко", "description": "1 л", "price": 80, "quantity": 3}
    )
    assert isinstance(p, Product)
    assert p.name == "Молоко"
    assert p.price == 80
    assert p.quantity == 3


def test_new_product_add_to_list():
    products = []
    p = Product.new_product(
        {"name": "Молоко", "description": "1 л", "price": 80, "quantity": 3}, products
    )
    assert len(products) == 1
    assert products[0] is p


def test_new_product_merge_duplicate():
    existing = [Product("Молоко", "1 л", 70, 5)]
    p = Product.new_product(
        {"name": "Молоко", "description": "1 л", "price": 90, "quantity": 2}, existing
    )
    assert len(existing) == 1
    assert existing[0].quantity == 7
    assert existing[0].price == 90
    assert p is existing[0]


def test_product_zero_quantity_raises():
    with pytest.raises(
        ZeroQuantityError, match="Товар с нулевым количеством не может быть добавлен"
    ):
        Product("Тестовый", "desc", 100, 0)
