# задание 1

import re

def check_car_number(number):
    car_number_pattern = re.compile(r'^[АВЕКМНОРСТУХ]\d{3}[АВЕКМНОРСТУХ]{2}\d{2,3}$')
    return "Частный" if car_number_pattern.match(number) else "Не номер"

def check_taxi_number(number):
    taxi_number_pattern = re.compile(r'^[АВЕКМНОРСТУХ]{2}\d{3}[АВЕКМНОРСТУХ]{2}\d{2,3}$')
    return "Такси" if taxi_number_pattern.match(number) else "Не номер"

# Примеры ввода
input_numbers = ["С227НА777", "КУ22777", "Т22В7477", "М227К19У9"]

# Проверка и вывод результата
for number in input_numbers:
    car_result = check_car_number(number)
    taxi_result = check_taxi_number(number)

    if car_result == "Частный":
        print("Частный")
    elif taxi_result == "Такси":
        print("Такси")
    else:
        print("Не номер")


#задание 2

import re

def count_words(text):
    word_pattern = re.compile(r'[А-Яа-яA-Za-z-]+')
    words = word_pattern.findall(text)
    return len(words)

# Пример ввода
input_text = "Он --- серо-буро-малиновая редиска!! >>>:-> А не ко"

# Подсчет слов и вывод результата
word_count = count_words(input_text)
print("Количество слов в тексте:", word_count)


#задвние 3

import re

def replace_time_with_tbd(text):
    time_pattern = re.compile(r'\b\d{2}:\d{2}(:\d{2})?\b')
    result_text = time_pattern.sub('(TBD)', text)
    return result_text

# Пример ввода
input_text = "Уважаемые! Если вы к 09:00 не вернёте чемодан, то уже в 09:00:01 я за себя не отвечаю. PS. С отношением 25:50 всё нормально!"

# Замена времени и вывод результата
output_text = replace_time_with_tbd(input_text)
print(output_text)
