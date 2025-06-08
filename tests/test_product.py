import pytest

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
