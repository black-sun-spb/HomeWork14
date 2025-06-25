from src.product import Product


def test_creation_logger_mixin_output(capfd):
    _ = Product("Продукт1", "Описание", 1200.0, 5)
    out, _ = capfd.readouterr()

    assert "Product" in out
    assert "'Продукт1'" in out
    assert "1200.0" in out
    assert "5" in out
