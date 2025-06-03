import pytest
from src.product import Product
from src.category import Category

@pytest.fixture(autouse=True)
def reset_class_attributes():
    # Сбросим счетчики перед каждым тестом, чтобы тесты были независимыми
    Category.category_count = 0
    Category.product_count = 0

def test_product_initialization():
    p = Product(name="Товар1", description="Описание1", price=10.5, quantity=3)
    assert p.name == "Товар1"
    assert p.description == "Описание1"
    assert p.price == 10.5
    assert p.quantity == 3

def test_category_initialization():
    p1 = Product("Товар1", "Описание1", 10.0, 1)
    p2 = Product("Товар2", "Описание2", 20.0, 2)
    cat = Category(name="Категория1", description="Описание категории", products=[p1, p2])

    assert cat.name == "Категория1"
    assert cat.description == "Описание категории"
    assert len(cat.products) == 2
    assert cat.products[0] == p1
    assert cat.products[1] == p2

def test_total_categories_and_products_count():
    p1 = Product("Товар1", "Описание1", 10.0, 1)
    p2 = Product("Товар2", "Описание2", 20.0, 2)

    cat1 = Category("Категория1", "Описание1", [p1])
    cat2 = Category("Категория2", "Описание2", [p2])

    assert Category.category_count == 2
    assert Category.product_count == 2

def test_category_products_length_matches_product_count():
    p1 = Product("Товар1", "Описание1", 10.0, 1)
    p2 = Product("Товар2", "Описание2", 20.0, 2)
    p3 = Product("Товар3", "Описание3", 30.0, 3)

    cat1 = Category("Категория1", "Описание1", [p1, p2])
    cat2 = Category("Категория2", "Описание2", [p3])

    # Общее число продуктов = 2 + 1 = 3
    assert Category.product_count == 3

    # Проверяем, что длина products у каждого объекта корректна
    assert len(cat1.products) == 2
    assert len(cat2.products) == 1
