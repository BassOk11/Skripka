"""number = int(input('Введите число: '))
if number % 3 == 0 and number % 5 == 0:
   print('FissBuzz')  # Наименее веротное решение лучше поместить в начало !!!!!
elif number % 3 == 0:   # Если выполнилось предыдущее условие то к следующему программа не переидёт
   print('Fizz')
elif number % 5 == 0:
   print('Buzz')

else:
   print('Неверное число')"""

number = int(input('Введите число 1: '))
number_1 = int(input('Введите число 2: '))
number_2 = int(input('Введите число 3: '))
if number == number_1 == number_2:
   print(3)
elif number != number_1 and number != number_2 and number_2 != number_1:
   print(0)
else:
   print(2)



