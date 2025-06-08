import pytest

from src.category import Category
from src.lawngrass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone


def test_same_product_addition():
    p1 = Product("Товар 1", "Описание", 100, 2)
    p2 = Product("Товар 2", "Описание", 50, 4)
    assert p1 + p2 == 100 * 2 + 50 * 4


def test_same_class_smartphone_addition():
    s1 = Smartphone(
        "iPhone", "Описание", 100000, 1, "высокая", "15 Pro", "256GB", "черный"
    )
    s2 = Smartphone("Samsung", "Описание", 80000, 2, "средняя", "S23", "128GB", "белый")
    assert s1 + s2 == 100000 + 160000


def test_mixed_class_addition_error():
    s = Smartphone(
        "iPhone", "Описание", 100000, 1, "высокая", "15 Pro", "256GB", "черный"
    )
    g = LawnGrass("Трава", "Газон", 500, 10, "Россия", "5 дней", "зеленый")
    with pytest.raises(TypeError, match="Складывать можно только товары одного типа"):
        _ = s + g


def test_category_add_product_invalid_type():
    cat = Category("Разное", "Товары", [])
    with pytest.raises(
        TypeError,
        match="Можно добавлять только объекты класса Product или его наследников",
    ):
        cat.add_product("Просто строка")


def test_category_add_product_valid_subclasses():
    cat = Category("Смартфоны", "Модели", [])
    s = Smartphone(
        "iPhone", "Описание", 100000, 1, "высокая", "15 Pro", "256GB", "черный"
    )
    g = LawnGrass("Трава", "Газон", 500, 10, "Россия", "5 дней", "зеленый")
    p = Product("Обычный товар", "Просто описание", 100, 3)

    cat.add_product(s)
    cat.add_product(g)
    cat.add_product(p)

    assert "iPhone" in cat.products
    assert "Трава" in cat.products
    assert "Обычный товар" in cat.products
