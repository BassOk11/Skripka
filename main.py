"""name = input('введите имя: ')
print('Здравствуйте: ',name,'!')
current_year = 2024
date_of_birth  = int(input('В каком годувы родились: '))
age = current_year - date_of_birth
print('В этом году вам: ',age,'лет')

print('зменяем регистр строки'.replace('регистр','незаменяем'))  #при помощи команды "upper" все буквы стали заглавные,"lower" преобразует в нижний

# списки
food = ['apple','cherry','meet','vodka']
print(food)
print(food[3])
food[1] = 'beer'
print(food)
food.append(True) #append добавляет слово в список
food.extend('рыба')
print(food)
food.remove('apple')
print(food)
print('coconat' in food)                #так можно проверить естьли значение в списке
print('coconate' not in food)          # а так нет ли его в списке
print(food[1:8:2])

    #кортеж
tuple_ = 1,2,3,4,5,6,7
print(tuple)
tuple_1 = (1,2,3,4,5,6,7,8)
print(tuple_1)
tuple_2 = tuple([1,2,3,4,5,6,7,])   #различные варианты создания кортежей
print(tuple_2)
print(type(tuple_))     #объекты внутри кортежа не изменяются, но с ним можно проводить математические операции


      #СЛОВАРи    (ключ : значение)
phone_book = {'Mars' : 9869305717, 'Nadin' : 9178990698, 'Bik' : 23234234}
print(phone_book)
phone_book ['Mars'] = 915098736     #изменть значение ключа
print(phone_book)
phone_book ['Den'] ='qwerqwer'      # Добавить новые данные в словарь
print(phone_book)
phone_book.update({'Sasha' : 'dsdfksdf' ,
                   'Masha' : True})  # Метод update добавляет несколько данных, рандомно
print(phone_book.get('Mars'))       # Мктод 'get' выводит значение поуказанному ключу
print(phone_book.get(' ','ключ отсутствует'))   #get ничего не выведет если ключ отсутствует
print(phone_book.pop('Den'))   # мктод pop достаёт значение указанного ключа, удалив ключ изсловаря
print(phone_book)
print(phone_book.keys())      # метод "keys" выводит список ключей, без значения
print(phone_book.values())     # метод "values" выводит толькосписок значений без ключа

    # Множества коллекция данных с уникальными значениями
set_ = {1,2,3,4,5,6,5,4,3,2,1,'str',True,}
print(set_)     #   Данные внутри множества не повторяются
                     # Так же "set" является методом образующим множество
list = (1,2,3,4,5,4,3,2,1)
print(set(list))   # с помощью функции "list" я превратил список в множество
list_ = set(list)  #еще вариант
print(list_)
                      # в множествах можно использовать теже функции


a = 5
print(a, "is of type", type(a))
a = 2.0
print(a, "is of type", type(a))
a = 1+2j
print(a, "is complex number?", isinstance(1+2j, complex))
print(type(a))

a = [5,10,15,20,25,30,35,40]
print("a[2] =", a[2])
print("a[0:3] =", a[0:3])


                  # (f) строка упрощает вывод
a = "123"
b = "23"
first = 'Вторник'
second = 'Понедельник'
print(f'{second}, {first},{a+b}')     # в f строке значения нужнобрать в фигурные скобки

              # условные операторы if, elif, else  устанавливают или проверяет условие, к примеру сравнение
a = 123
b = 321
if a<b:                   # после условного Оп. надо ставить двоеточие
    print('А меньше Б')
if a>b:
    print('А больше б')

a = 15
b = 10
c = 15
if a==c!=b or b==c!=a:  # условие не выполнилось и программа перешла к elif [a=с и не равно b] или [b=c и не равно a]
    print(1)
elif a==b==c and a==b!=c: # здесь условие не выполнилось снова тогда переход к else
    print(2)               # есть еще разница между or и and
else:
    print(0)    #можно менять значение переменных и получатьразные результаты

a = int(input('введи любое число: '))
b = int(input('второе любое число: '))  #внимание не забыть input дает тип данных СТРОКА!!!
if a<b:
    print(a)
if a>b:
    print(b)


          # Списки снова!!!!
a = []
a.append('a')
a.append(2)
a.append('b')
a.append('3')
print(a)
print(a[2])
print(a[::-1])"""

string = input('Напишите что нибудь: ')
a = string.upper()
b = string.lower()
print((len(string), a, b))





