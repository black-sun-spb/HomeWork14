import pytest

from src.exceptions import ZeroQuantityError
from src.product import Product


def test_product_raises_zero_quantity_error():
    with pytest.raises(
        ZeroQuantityError, match="Товар с нулевым количеством не может быть добавлен"
    ):
        Product("Тестовый", "desc", 100, 0)
