# Задача 16: Требуется вычислить, сколько раз встречается некоторое число
# X в массиве A[1..N]. Пользователь в первой строке вводит натуральное 
# число N – количество элементов в массиве. В последующих  строках 
# записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     3
#     -> 1

n = int(input("Введите число элементов в массиве: "))
list1 = []
list1 = list(input("Введите элементы массива через запятую: ").split(','))
if len(list1) != n:
    print(f"Количество веденных элементов массива должно быть {n}")
else:
    for i in range(n):
        list1[i] = int(list1[i])
    print(list1)
    x = int(input("Введите число Х: "))
    count = 0
    for i in range(n):
        if list1[i] == x:
            count += 1
print(f'Число {x} встречается в заданном массиве {count} раз') 