# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть
import random

def find_min_flip_coins(list_coins):
    count_tails, count_eagle = 0, 0
    for i in list_coins:
        if i in "Герб":
            count_eagle += 1
        else:
            count_tails += 1
    return min(count_tails, count_eagle)





count_coins = int(input("Введите кол-во монет: "))

list_coins = [random.choice(("Герб", "Решка")) for i in range(count_coins)]

print(*list_coins)

print(f"Минимальное кол-во монет которых нужно перевернуть для, чтобы монеты лежали вверх одной стороной -->> {find_min_flip_coins(list_coins)}")