# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. 
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

import random

# Описание вывода решения:
# sum = x + y
# product = x * y
# x = sum - y
# product = (sum - y) * y
# product = sum*y - y**2
# y**2 - sum*y - P = 0
# Дальше решаем квадратное уравнение в функции find_hundders_numbers

def protect_input(message):
    print(message)
    num = input()
    if num.isdigit():
        return int(num)
    return protect_input("Ввели не число. Повторите попытку: ")


def find_hundders_numbers(sum, product):
    
    diskriminant = sum**2 - 4*1*product
    
    one_number = (sum - diskriminant**0.5) / 2
    two_number = (sum + diskriminant**0.5) / 2

    return one_number, two_number



sum, product = protect_input("Введите сумму загаданных чисел: "), protect_input("Введите произведение загаданных чисел: ")


print(f"Числа, которые загадал Петя --> {find_hundders_numbers(sum, product)}")