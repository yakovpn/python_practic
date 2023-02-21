# Задача 26: Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

def power(a, b):
    if (b == 1):
        return a
    if (b != 1):
        return (a * power(a, b - 1))


def homework01():
    a = int(input("Введите число:"))
    b = int(input("Введите его степень:"))
    print("Результат возведения в степень равен:", power(a, b))

# homework01()

# Задача 28: Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел. Из
# всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.
# 2 2
# 4

# a+1 b-1
# b=0 вернуть a

def sum(a, b):
    if b == 0:
        return a
    return sum(a+1, b-1)


def homework02():
    a = int(input("Введите число a:"))
    b = int(input("Введите число b:"))
    print(f'Сумма {a} + {b} = {sum(a,b)}')


# homework02()