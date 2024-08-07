import random
number = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
c = random.choice(number)
print(c)
b = 0
passw = ""
for i in range(1, c):
    for j in range(i + 1, c):
        if c % (i + j) == 0:
            passw += str(i) + str(j)
print(passw)















