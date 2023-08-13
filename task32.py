# Задача 32: Определить индексы элементов массива (списка), значения которых 
# принадлежат заданному диапазону (т.е. не меньше заданного минимума и не 
# больше заданного максимума). Список можно задавать рандомно
# На входе : [ 1, 5, 88, 100, 2, -4]
# 33
# 200
# Ответ: [2, 3]

import random

min_val = int(input("Введите минимум диапазона: "))
max_val = int(input("Введите максимум диапазона: "))
list_1 = []
indices = []

for i in range(10):
    list_1.append(random.randint(-100,501))

def find_index(list):
    for i in list_1:
        if    min_val <= i <= max_val:
            indices.append(list_1.index(i))
    return indices

print(find_index(list_1))
 