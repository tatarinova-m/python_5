#Задача 30:  Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.


first_element = int(input("Введите первый элемент массива: "))
amount = int(input("Введите кол-во элементов: "))
dif = int(input("Введите разность прогрессии: "))
list_1 = []

def find_progress(a1,n,d):
    for i in range(n):
        if n > 0:
            res = a1 + (n-1) * d
            list_1.append(res)
            n -= 1
        else :
            return list_1
find_progress(first_element,amount,dif)
result = sorted(list_1)
print(*result)