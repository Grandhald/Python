# Требуется вывести все целые степени двойки (т.е. числа вида 2^k), не превосходящие числа N.

def protect_input(message):
    print(message)
    num = input()
    if num.isdigit():
        return int(num)
    return protect_input("Ввели не число. Повторите попытку: ")


number, power= protect_input("Введите число: "), 0

print(f"Все целые степени двойки до числа не превосходящие число {number}: ")

while 2**power <= number:
    print(2**power, end = " ")
    power += 1
