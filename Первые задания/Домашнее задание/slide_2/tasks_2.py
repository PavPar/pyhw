# 1.Найти N-й член последовательности 1, 1, 2, 3, 5, 8, 13...
def fib(n):
    fib = [1, 1]
    for i in range(2, n + 1):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib[n]


# 2.Найти N-й член последовательности 1, 1, 1, 3, 5, 9, 17...

def fib_2(n):
    fib = [1, 1, 1]  # А почему нет?
    for i in range(3, n + 1):
        fib.append(fib[i - 1] + fib[i - 2] + fib[i - 3])
    return fib[n]


# 3.Вывести квадраты нечетных чисел до N. (генератором списков)

def gen(n):
    return [i ** 2 for i in range(0, n + 1) if (i % 2 != 0)]


# 4.Вычислить сумму и произведение всех натуральных чисел от А до В
# включительно.
from functools import reduce


def gen_1(a, b):
    arr = [i for i in range(a, b + 1)]
    return [sum(arr), reduce(lambda x, y: x * y, arr), arr]


# 5. Даны натуральные числа А и В. Вывести сначала все чётные числа, заключённые
# между ними, потом все нечётные (генератором/ами списков)

def gen_2(a, b):
    arr1 = [i for i in range(a, b + 1) if (i % 2 == 0)];
    arr2 = [i for i in range(a, b + 1) if (i % 2 != 0)]
    return arr1 + arr2


# 6. Исходный список содержит положительные и отрицательные числа. Требуется
# положительные поместить в один список, а отрицательные - в другой
# (генератором/ами списков)

def gen_3(oldArr):
    arr1 = [i for i in oldArr if (i < 0)];
    arr2 = [i for i in oldArr if (i >= 0)]
    return [arr1,arr2]


print('задание 1:')
print(fib(7))

print('задание 2:')
print(fib_2(6))

print('задание 3:')
print(gen(5))

print('задание 4:')
print(gen_1(2, 5))

print('задание 5:')
print(gen_2(0, 10))

print('задание 6:')
print(gen_3([-1, -2, -3, 5, 6, 1, -2, -3]))
