# Нужно реализовать Польскую нотацию для двух положительных чисел
# С помощью выражения assert проверять, что первая операция в списке доступных операций (+, -, *, /). С помощью конструкций try/expcept ловить ошибки и выводить предупреждения Типы ошибок

operator_list = ["+", "-", "*", "/"]
try:
    operator, number_1, number_2 = map(str, input("Введите арифметический оператор и два числа: ").split())
    number_1 = int(number_1)
    number_2 = int(number_2)
except (ValueError, NameError):
    print("Неверное количество аргументов!")
else: 
    assert operator in operator_list, "operator is not found"

try:
    if operator == "+":
        print(f"Результат равен: {number_1 + number_2}")
    elif operator == "-":
        print(f"Результат равен: {number_1 - number_2}")
    elif operator == "*":
        print(f"Результат равен: {number_1 * number_2}")
    elif operator == "/" or ":":
        integer_number = int(number_1 / number_2)
        print(f"Результат равен: {integer_number}")
except ZeroDivisionError:
    print("На ноль делить нельзя!")
except TypeError:
    print("Ошибка типа!")
except NameError:
    print("Вычисление невозможно, оператор не определен!")