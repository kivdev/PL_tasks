from math import sqrt
import sys

data = [[], []]

# Имя входного файла
files = sys.argv[-2:]
# Читаем файлы
for i, file in enumerate(files):
    with open(file, 'r', encoding='utf-8') as f:
        for line in f:
            # Записываем координаты в кортежи
            data[i].append((float(line.split(' ')[0].strip()), float(line.split(' ')[1].strip())))
# Преобразуем список координат четырехугольника во множество
data_set = set(data[0])
for i in data[1]:
    # Точка на одной из вершин
    if i in data_set:
        print(0)
        continue
    else:
        # Приналжежность точки стороне
        lineLen = sqrt((data[0][1][0] - data[0][0][0]) ** 2 + (data[0][1][1] - data[0][0][1]) ** 2)
        lenPointToLeft = sqrt((data[0][1][0] - i[0]) ** 2 + (data[0][1][1] - i[1]) ** 2)
        lenPointToRight = sqrt((data[0][0][0] - i[0]) ** 2 + (data[0][0][1] - i[1]) ** 2)
        if lenPointToLeft + lenPointToRight == lineLen:
            print(1)
            continue
        lineLen = sqrt((data[0][2][0] - data[0][1][0]) ** 2 + (data[0][2][1] - data[0][1][1]) ** 2)
        lenPointToLeft = sqrt((data[0][2][0] - i[0]) ** 2 + (data[0][2][1] - i[1]) ** 2)
        lenPointToRight = sqrt((data[0][1][0] - i[0]) ** 2 + (data[0][1][1] - i[1]) ** 2)
        if lenPointToLeft + lenPointToRight == lineLen:
            print(1)
            continue
        lineLen = sqrt((data[0][3][0] - data[0][2][0]) ** 2 + (data[0][3][1] - data[0][2][1]) ** 2)
        lenPointToLeft = sqrt((data[0][3][0] - i[0]) ** 2 + (data[0][3][1] - i[1]) ** 2)
        lenPointToRight = sqrt((data[0][2][0] - i[0]) ** 2 + (data[0][2][1] - i[1]) ** 2)
        if lenPointToLeft + lenPointToRight == lineLen:
            print(1)
            continue
        lineLen = sqrt((data[0][0][0] - data[0][3][0]) ** 2 + (data[0][0][1] - data[0][3][1]) ** 2)
        lenPointToLeft = sqrt((data[0][0][0] - i[0]) ** 2 + (data[0][0][1] - i[1]) ** 2)
        lenPointToRight = sqrt((data[0][3][0] - i[0]) ** 2 + (data[0][3][1] - i[1]) ** 2)
        if lenPointToLeft + lenPointToRight == lineLen:
            print(1)
            continue
        # Определяем положение точки относительно четырехугольника
        intersection = 0
        for j in range(len(data[0])):
            if (((data[0][j][1] <= i[1] < data[0][j - 1][1]) or
                 (data[0][j - 1][1] <= i[1] < data[0][j][1])) and
                    (i[0] > (data[0][j - 1][0] - data[0][j][0]) * (i[1] - data[0][j][1]) / (
                            data[0][j - 1][1] - data[0][j][1]) + data[0][j][0])):
                intersection += 1
        if intersection % 2 == 0:
            print(3)
            continue
        else:
            print(2)
            continue
