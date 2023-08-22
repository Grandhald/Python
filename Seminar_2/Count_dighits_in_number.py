# Задача 1 HARD по желанию Напишите программу,
# которая принимает на вход целое или дробное число и выдаёт количество цифр в числе.
# 456 -> 3
# 0 -> 1
# 89,126 -> 5
# 0,001->4



import decimal


def protect_input(message):
    try:
        num = decimal.Decimal(input(message))
        return num
    except:
        return protect_input("Вы ввели не число. Повторите попытку: ")

def count_dighits_in_num(number):
    count = 1
    while number % 10 != int(number % 10):
        number *= 10
    
    while number % 10 != number:
        count += 1
        number //= 10
    
    return count






number = protect_input("Введите число: ")
print(number)
print(f"Кол-во цифр в числе {number} -->> {count_dighits_in_num(number)}")