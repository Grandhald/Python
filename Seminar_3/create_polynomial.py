# Пользователь вводит натуральное k. Надо сформировать многочлен такой степени, где все коэффициенты случайные от -10 до 10.

# например, k=2 -> -x^2 + 3*x - 8 = 0
# тут коэффициенты -1,3,-8
# например, k=3 -> 3*x^3 - 2*x = 0
# тут коэффициенты 3,0,-2,0
from random import randint as rnd




def create_polynominal(k):
    all_dick =""
    koof_list = list()

    while k != -1: 
        koof = rnd(-10, 10)
        koof_list.append(koof)
        znak = ("+" if koof > 0 else "-") 
              
        if koof == 0: 
            continue
        elif k == 1:  
            all_dick += f"{znak} {abs(koof)} * x "
        elif k == 0: 
            all_dick += f"{znak} {abs(koof)}"
        elif koof == 1 or koof == -1: 
            all_dick += f"{znak} x ^ {k}"
        else:   
            all_dick += f"{znak} {abs(koof)} * x ^ {k} "
        
        k -= 1
    if all_dick[0] == "+":
        all_dick = all_dick[1: ]
    all_dick += " = 0"
    
    return all_dick, koof_list
        
        
    





k = int(input())

polynominal_k = create_polynominal(k)   

print(*polynominal_k, sep= "\n")
