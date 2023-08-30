def trans_doub_to_octava(num, typ_system):
    number = num 
    list_digits = []
    while number > 0:
        list_digits.append(number % typ_system)
        number //= typ_system
    list_digits.reverse()
    return list_digits



number = int(input("Введите в число: "))

typ_sys = int(input("Введите числом систему исчесления, в которую хотите перевести: "))

print(*trans_doub_to_octava(number, typ_sys), sep = "")
