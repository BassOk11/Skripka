"""def print_params(a, b, c, d):  # *args  1 звезда запаковка позиционных параметров с 1м элементом.
    print(a, b, c, d)    # ** 2 звезды запаковываки именованных параметров в словарь (ключь : значение)


dact = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print_params(**dact)


def print_params(**kwargs):  # kwargs дает нам при вызове функции словарь
    print(kwargs)    # ** 2 звезды запаковываки именованных параметров в словарь (ключь : значение)
    for key, value in kwargs.items():
        print(key)

dact = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print_params(**dact)


def test_funk(*test):
    print('Тип: ',type(test))
    print('Аргумент: ', test)


test_funk(1, 2, 3, 4)


def summstor(txt, *values, type_='summ'):
    s = 0
    for i in values:
        s += i
    return f'{txt}{s}{type_}'


print(summstor('сумма чисел: ', 1, 2, 3, 4, type_='summator'))


def info(**values):
    print('Тип: ', type(values))
    print('Аргумент: ', values)
    for key, value in values.items():
        print(key, value)
info(name=input('Введите имя: ') , curse='python')"""

def my_summ(n, *args, txt="Сумма чисел "):
    s = 0
    for i in range(len(args)):
        s += args[i] ** n
    print(txt + ":", s)


my_summ(2,1, 2, 3, 4, 5, txt="Квадрат чисел")
