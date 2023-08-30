# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть
import random

def protect_input(message):
    print(message)
    num = input()
    if num.isdigit():
        return int(num)
    return protect_input("Ввели не число. Повторите попытку: ")


def find_min_flip_coins(list_coins):
    count_tails, count_eagle = 0, 0
    for i in list_coins:
        if i in "Герб":
            count_eagle += 1
        else:
            count_tails += 1
    return min(count_tails, count_eagle)





count_coins = protect_input("Введите кол-во монет: ")

list_coins = [random.choice(("Герб", "Решка")) for i in range(count_coins)]

print(*list_coins)

print(f"Минимальное кол-во монет которых нужно перевернуть для, чтобы монеты лежали вверх одной стороной -->> {find_min_flip_coins(list_coins)}")


if list_coins.count("Герб") > list_coins.count("Решка"):
    print(list_coins.count("Решка"))
else: 
    print(list_coins.count("Герб"))