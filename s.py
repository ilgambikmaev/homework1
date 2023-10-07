def sum_range(start, end):
    if start > end:
        start, end = end, start

    total = 0


    for number in range(start, end + 1):
        total += number

    return total


result = sum_range(5, 80)
print(result)



import math

def square(side):
    # Рассчитываем периметр
    perimeter = 4 * side

    # Рассчитываем площадь
    area = side * side

    # Рассчитываем диагональ с помощью теоремы Пифагора
    diagonal = math.sqrt(2) * side

    # Возвращаем результат в виде кортежа
    return (perimeter, area, diagonal)

# Пример использования функции
side_length = 5
result = square(side_length)
print("Периметр:", result[0])
print("Площадь:", result[1])
print("Диагональ:", result[2])


def bank(a, years):
    # Изначальный вклад
    principal = a

    # Годовая процентная ставка
    annual_interest_rate = 0.10

    # Вычисляем сумму на счету после указанного количества лет
    for _ in range(years):
        principal += principal * annual_interest_rate

    return principal



initial_deposit = 1000  # Начальный вклад в рублях
investment_period = 5  # Срок вложения в годах
final_amount = bank(initial_deposit, investment_period)
print("Итоговая сумма на счету:", final_amount, "рублей")



def encode_to_unicode(input_string):
    encoded_string = ""
    for char in input_string:
        encoded_string += f"\\u{ord(char):04x}"
    return encoded_string

input_string = "Привет, мир!"
encoded_result = encode_to_unicode(input_string)
print(encoded_result)



check_parity = lambda num: "Четное" if num % 2 == 0 else "Нечетное"


print(check_parity(10))
print(check_parity(7))