class ErrorResponse(Exception):
    """Класс исключения для ошибки запроса."""

    def __init__(self, *args) -> None:
        """
        Конструктор класса ErrorResponse.

        :param args: Произвольное количество позиционных аргументов,
        используемых для установки сообщения об ошибке.
        """
        self.message = args[0] if args else "Ошибка выполнения запроса"

    def __str__(self) -> str:
        """Возвращает строковое сообщение об ошибке."""
        return self.message
