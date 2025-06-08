import pytest

from src.category import Category
from src.lawngrass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone


@pytest.fixture(autouse=True)
def reset_class_attributes():
    Category.category_count = 0
    Category.product_count = 0


def test_add_product_and_private_products():
    cat = Category("Овощи", "Свежие овощи", [])
    product = Product("Морковь", "Сочная", 50, 10)
    cat.add_product(product)

    assert "Морковь" in cat.products


def test_products_getter_format():
    cat = Category("Фрукты", "Сладкие", [])
    product = Product("Яблоко", "Красное", 80, 15)
    cat.add_product(product)

    expected = "Яблоко, 80 руб. Остаток: 15 шт."
    assert expected in cat.products


def test_category_str_total_quantity():
    cat = Category("Фрукты", "Разные фрукты", [])
    cat.add_product(Product("Яблоко", "Красное", 80, 15))
    cat.add_product(Product("Банан", "Желтый", 60, 5))

    assert str(cat) == "Фрукты, количество продуктов: 20 шт."


def test_add_only_product_subclasses():
    cat = Category("Тест", "Проверка", [])
    cat.add_product(
        Smartphone(
            "iPhone", "Описание", 100000, 3, "Pro Max", "256GB", "Модель X", "Серый"
        )
    )
    cat.add_product(
        LawnGrass("Green Mix", "Описание", 900, 10, "Россия", "2 недели", "Зеленый")
    )

    with pytest.raises(
        TypeError,
        match="Можно добавлять только объекты класса Product или его наследников",
    ):
        cat.add_product("не продукт")
