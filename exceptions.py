# exceptions.py

class InvalidValueError(Exception):
    """Пользовательское исключение для недопустимого значения"""
    pass

class DivisionByZeroError(Exception):
    """Пользовательское исключение для деления на ноль"""
    pass

class OperationNotSupportedError(Exception):
    """Пользовательское исключение для неподдерживаемой операции"""
    pass
