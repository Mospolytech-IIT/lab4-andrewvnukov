# functions.py

from exceptions import InvalidValueError, DivisionByZeroError, OperationNotSupportedError

# Шаг 1: Функции, выбрасывающие исключения без обработчиков

def divide(a, b):
    """Делит число a на число b, выбрасывает исключение при делении на ноль"""
    if b == 0:
        raise ZeroDivisionError("Деление на ноль невозможно.")
    return a / b

def get_item_from_list(lst, index):
    """Возвращает элемент списка по индексу, выбрасывает исключение при выходе за границы"""
    if index >= len(lst):
        raise IndexError("Индекс за пределами списка.")
    return lst[index]

# Шаг 2: Функция с одним обработчиком исключений общего типа

def safe_divide(a, b):
    """Безопасное деление с общим обработчиком исключений"""
    try:
        return a / b
    except Exception as e:
        print(f"Ошибка: {e}")
        return None

# Шаг 3: Функция с обработчиком и finally-блоком

def parse_int(value):
    """Пытается преобразовать значение в целое число, обрабатывает ошибки и завершает работу корректно"""
    try:
        return int(value)
    except Exception as e:
        print(f"Ошибка преобразования: {e}")
        return None
    finally:
        print("Завершение функции parse_int.")

# Шаг 4: Функции с несколькими типами обработчиков исключений

def calculate(a, b, operation):
    """Выполняет математическую операцию и обрабатывает несколько типов исключений"""
    try:
        if operation == "divide":
            return divide(a, b)
        elif operation == "multiply":
            return a * b
        elif operation == "subtract":
            return a - b
        elif operation == "add":
            return a + b
        else:
            raise OperationNotSupportedError("Операция не поддерживается.")
    except ZeroDivisionError:
        print("Попытка деления на ноль.")
        return None
    except TypeError:
        print("Неправильный тип данных.")
        return None
    except OperationNotSupportedError as e:
        print(f"Ошибка: {e}")
        return None
    finally:
        print("Выполнение функции calculate завершено.")

# Шаг 5: Функция, выбрасывающая и обрабатывающая свои исключения

def validate_value(value):
    """Проверяет значение и выбрасывает исключения при нарушении правил"""
    try:
        if not isinstance(value, int):
            raise InvalidValueError("Значение должно быть целым числом.")
        if value < 0:
            raise ValueError("Значение не может быть отрицательным.")
        if value == 0:
            raise DivisionByZeroError("Значение не может быть нулём.")
    except (InvalidValueError, ValueError, DivisionByZeroError) as e:
        print(f"Ошибка валидации: {e}")
        return None
    finally:
        print("Функция validate_value завершена.")

# Шаг 7: Функция, выбрасывающая пользовательское исключение и обрабатывающая его

def check_positive(value):
    """Проверяет, является ли число положительным, выбрасывает пользовательское исключение при ошибке"""
    try:
        if value <= 0:
            raise InvalidValueError("Число должно быть положительным.")
        return value
    except InvalidValueError as e:
        print(f"Ошибка: {e}")
        return None
    finally:
        print("Функция check_positive завершена.")

# Шаг 8: Дополнительные функции для демонстрации работы исключений

def multiply_positive_numbers(a, b):
    """Умножает два положительных числа, проверяя на положительность"""
    check_positive(a)
    check_positive(b)
    return a * b

def subtract_nonzero(a, b):
    """Вычитает числа, проверяя, что ни одно из них не является нулём"""
    validate_value(a)
    validate_value(b)
    return a - b

def complex_operation(a, b):
    """Выполняет сложную операцию с использованием нескольких других функций"""
    try:
        result = divide(a, b)
        return multiply_positive_numbers(result, a)
    except Exception as e:
        print(f"Ошибка комплексной операции: {e}")
