from src.lawngrass import LawnGrass
from src.smartphone import Smartphone


def test_smartphone_inheritance():
    phone = Smartphone(
        name="iPhone 15",
        description="Новый флагман Apple",
        price=120000,
        quantity=5,
        efficiency="высокая",
        model="15 Pro",
        memory="256GB",
        color="черный",
    )

    assert phone.name == "iPhone 15"
    assert phone.description == "Новый флагман Apple"
    assert phone.price == 120000
    assert phone.quantity == 5
    assert phone.efficiency == "высокая"
    assert phone.model == "15 Pro"
    assert phone.memory == "256GB"
    assert phone.color == "черный"


def test_lawngrass_inheritance():
    grass = LawnGrass(
        name="Зеленая поляна",
        description="Газонная трава",
        price=1500,
        quantity=10,
        country="Россия",
        germination_period="5-7 дней",
        color="зеленый",
    )

    assert grass.name == "Зеленая поляна"
    assert grass.description == "Газонная трава"
    assert grass.price == 1500
    assert grass.quantity == 10
    assert grass.country == "Россия"
    assert grass.germination_period == "5-7 дней"
    assert grass.color == "зеленый"
