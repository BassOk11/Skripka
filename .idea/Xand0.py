def draw_area():
    for i in area:
        print(*i)
    print()
area = [['* ','* ','* '],['* ','* ','* '],['* ','* ','* ']]
print('Добро пожаловать в крестики нолики!')
print('_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_')
draw_area()
for turn in range(1, 10):
    print(f'Ход: {turn}')
    if turn % 2 == 0:
        turn_char = '0 '
        print('Ходят нолики')
    else:
        turn_char = 'X '
        print('Ходят крестики')
# с помощью функции def мы распаковали вложенныйсписок area

#area[0][0] = 'X '   #иксом стал символ с инд.0 вовложеннлм списке с инд.0
    row = int(input('Введите номер строки (1, 2, 3) ')) - 1
    colum = int(input('Введите номер столбца (1, 2, 3) ')) - 1
    if area[row][colum] == '* ':
        area[row][colum] = turn_char
    else:
        print('Ячейка занята, вы пропускаете ход')
        draw_area()
        continue

    draw_area()
"""def chec_winner():
    if area[0][0] == 'X ' and area[0][1] =='X ' and area[0][2] == 'X ':
        return 'X'
    if area[1][0] == 'X ' and area[1][1] == 'X ' and area[1][2] == 'X ':
        return 'X'
    if area[2][0] == 'X ' and area[2][1] =='X ' and area[2][2] == 'X ':
        return 'X'
    if area[0][1] == 'X ' and area[1][1] =='X ' and area[2][1] == 'X ':


    whinn_X = 'Победили крестики'
    whinn_O = 'Победили нолики'"""


