import random


def password():
    pass_ = ''
    for i in range(1, num):
        for j in range(i + 1, num):
            if (i + j) % num == 0:
                pass_ += str(i) + str(j)
    return pass_


numbers = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
num = random.choice(numbers)
print(num)
print(password())
