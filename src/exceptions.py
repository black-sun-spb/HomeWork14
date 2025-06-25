# exceptions.py
class ZeroQuantityError(Exception):
    """Ошибка, если у товара нулевое количество."""

    def __init__(self, message="Товар с нулевым количеством не может быть добавлен"):
        super().__init__(message)
