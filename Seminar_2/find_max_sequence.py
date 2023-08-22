# Задача VERY HARD необязательная
# Имеется список случайных целых чисел. Создайте список, в который попадают числа,
# описывающие максимальную сплошную возрастающую последовательность. 
# Порядок элементов менять нельзя.
# Одно число - это не последовательность.

# Пример:

# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 7] так как здесь вразброс присутствуют все числа от 1 до 7

# [1, 5, 2, 3, 4, 1, 7, 8 , 15 , 1 ] => [1, 5] так как здесь есть числа от 1 до 5 и эта последовательность длиннее чем от 7 до 8

# [1, 5, 3, 4, 1, 7, 8 , 15 , 1 ] => [3, 5] так как здесь есть числа от 3 до 5 и эта последовательность длиннее чем от 7 до 8


import random


def find_max_sequence(list):
    list_number = list.copy()
    max_sequence = []
    print(f"{sorted(set(list_number))} - отсортированная последовательность с удалением повторяющихся элементов")
    while len(list_number) > 0:
        index = list_number.index(min(list_number))
        sequence = [list_number[index]]
        while sequence[-1]+1 in list_number:
            sequence.append(sequence[-1]+1)
        if len(max_sequence) <= len(sequence): 
            max_sequence = sequence.copy()
        list_number.pop(index)
    if len(max_sequence) < 2:
        return "в списке нет последовательности чисел"
    return [max_sequence[0], max_sequence[-1]]



for i in range(100):
    list_num = [random.randrange(0,20) for i in range(20)]
    print(f"{list_num} - изначальная последовательность" )
    max_sequence = find_max_sequence(list_num)
    print(max_sequence)
    print()
