# main.py

from functions import (
    divide,
    get_item_from_list,
    safe_divide,
    parse_int,
    calculate,
    validate_value,
    check_positive,
    multiply_positive_numbers,
    subtract_nonzero,
    complex_operation
)

def main():
    print("Добро пожаловать в калькулятор!\n")

    # Пример значений, которые могли бы быть введены пользователем
    a, b = 10, 0  # a и b – два числа для расчетов
    operation = "divide"  # Операция, выбранная пользователем (например, деление)

    # Шаг 1: Проверка значений для положительных чисел и недопустимых значений
    print("Шаг 1: Проверка значений на положительность и допустимость")
    try:
        check_positive(a)
        check_positive(b)
        validate_value(a)
        validate_value(b)
    except Exception as e:
        print(f"Ошибка ввода данных: {e}")
        return  # Завершить выполнение, если проверка не пройдена

    # Шаг 2: Выполнение выбранной операции
    print("\nШаг 2: Выполнение операции")
    try:
        result = calculate(a, b, operation)
        print(f"Результат операции '{operation}' для чисел {a} и {b}: {result}")
    except Exception as e:
        print(f"Ошибка при выполнении операции: {e}")

    # Шаг 3: Дополнительные операции и тестирование других функций
    print("\nШаг 3: Выполнение других операций")
    try:
        # Пример: Умножение положительных чисел
        multiplication_result = multiply_positive_numbers(a, 5)
        print(f"Результат умножения: {multiplication_result}")

        # Пример: Проверка разности чисел с условием, что они не равны нулю
        subtraction_result = subtract_nonzero(a, 3)
        print(f"Результат вычитания: {subtraction_result}")

        # Пример: Сложная операция (деление с последующим умножением)
        complex_result = complex_operation(a, b)
        print(f"Результат комплексной операции: {complex_result}")
    except Exception as e:
        print(f"Ошибка при выполнении дополнительной операции: {e}")

    print("\nВсе операции выполнены корректно. Калькулятор завершил работу.")

if __name__ == "__main__":
    main()
