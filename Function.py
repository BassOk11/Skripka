"""def calc(num1, num2):
    def summ():
        print(num1 + num2)

    def minus():
        print(num1 - num2)

    def umn():
        print(num1 * num2)

    def del_():
        print(num1 / num2)

    print('1, +')
    print('2, -')
    print('3, *')
    print('4, /')
    operation = int(input('Select operation: '))
    if operation == (1):
        summ()
    elif operation == 2:
        minus()
    elif operation == 3:
        umn()
    elif operation == 4:
        del_()
    else:
        print("Некорректная операция")


num1 = int(input('Число 1: '))
num2 = int(input('Число 2: '))
calc(num1, num2)
"""
"""def calc1():
    num3 = int(input('Число 1: '))
    num4 = int(input('Число 2: '))
    print('1, +')
    print('2, -')
    print('3, *')
    print('4, /')
    operation = int(input('Select operation: '))
    def plus():
        if operation == 1:
            print(num3 + num4)
    plus()
calc1()

def reg(name):
    print('Hello ', name)
    name = 'Ivan'
    print('Hello ', name)
name = 'Vfhctkm'
reg(name)"""

import random


def funk():  # создалосновную функция
    rnum = random.randint(1, 100)  # создалрандомную переменную

    def first(rnum):  # присвоил вкачестве аргумента переменнуюдля функции
        print(rnum ** 2)  # внутри функции действие

    def seccund(rnum):  #присвоиларгумент для другой функции
        print(rnum // 2)  #внутри функции действие

    print(rnum)  #распечатал переменную для проверки
    if rnum > 50:  #создал условие
        first(rnum)  # в случае выполнения вызвал первую функцию
    else:  # создалдругой аргумент
        seccund(rnum)  # вызвал вторую функцию


funk() # вызов всей функции
