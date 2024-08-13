"""a = int(input("Введите число А: "))
b = int(input("Введите число Б "))
if a >= b:
    while a >= b:
        print(a)
        a -= 1
else:
    while a <= b:
        print(a)
        a += 1
if a >= b:
    while a >= b:
        print(a)
        a -= 1
print("конец")"""

"""k = []
while len(k) < 5:
    r = int(input("Введите число: "))
    k.append(r)
print(k)


print()
"""
list_1 = []
list_2 = []
list_3 = []
num = int(input("Введите цыфру: "))
for i in range(num):
    num2 = int(input('Numm: '))
    if num2 % 3 == 0 and num2 % 5 == 0:
        list_2.append(num2)
    elif num2 % 2 == 0 or num2 % 3 == 0:
        list_1.append(num2)
    else:
        list_3.append(num2)


print(list_1)
print(list_2)
print(list_3)




