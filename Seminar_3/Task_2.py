# В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, причём кусты высажены только по окружности.
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью,
# поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло a[i] ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом,
# собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод,
# которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном списке урожайности грядки.
from random import randint as rnd


def find_count_berries(list_product):
    count_bush = list_product[len(list_product)-2: ] + list_product[: 1]
    temp = list_product[len(list_product)-1: ] + list_product[: 2]
    if sum(temp) > sum(count_bush):
        count_bush = list_product[len(list_product)-1: ] + list_product[: 2]
    for i in range(len(list_product)-1):
        temp = list_product[i-1: i+2]
        if sum(temp) > sum(count_bush):
           count_bush = temp    
    return count_bush, sum(count_bush)

def create_random_list(len_list):
    list_random = [rnd(0, 5) for i in range(len_list)]
    return list_random




count_bush = int(input("Введите количество кустов: "))
list_product_bush = create_random_list(count_bush)


print(list_product_bush)

print(find_count_berries(list_product_bush))