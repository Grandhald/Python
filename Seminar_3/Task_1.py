# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества.
# m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

from random import randint as rnd

def sequence_intersection(sequence_first, sequence_second):
    intsec_seq = set(sequence_first).intersection(sequence_second)
    return sorted(list(set(sequence_first).intersection(sequence_second)))

def create_random_sequence(len_seq):
    list_sequence = [rnd(-10, 10) for i in range(len_seq)]
    return list_sequence

seq_first = create_random_sequence(int(input("Введите длину первой последовательности:  "))) 
seq_sec = create_random_sequence(int(input("Введите длину второй последовательности:  ")))
intsec_seq = sequence_intersection(seq_first, seq_sec)
print(*seq_first), print(), print(*seq_sec)
print()
print(*("Нет общих чисел", intsec_seq)[len(intsec_seq) != 0])