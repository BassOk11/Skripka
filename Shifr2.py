def parol(number):
    parol_1 = ""
    number = int(input("Введите число от 3 до 20: "))

    for i in range(1, number):
        for j in range(i + 1, number):
            if number % (i + j):
                parol_1 += str(i) + str(j)
    return parol_1
i = 3
while i < 21:
    print(parol(i))
    i += 1
