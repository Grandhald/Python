# Задача НЕГАФИБОНАЧЧИ по желанию
# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]



def fib(n):
    num_fib = [1, 0, 1]
    
    if n <= 2:
        if n == 2:
            return num_fib
        elif n == 1:
            return [0]
        else: 
            return[]  
            
    for i in range(n-1):
        pow = (-1)**(i+1)
        num_fib.append(num_fib[-1]+ num_fib[-2])
        num_fib = [num_fib[-1]*pow] + num_fib
        
    return num_fib



print(fib(int(input("Введите число последовательность Фиббоначи: "))))