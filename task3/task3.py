import sys
import os
data = [[],
        [],
        [],
        [],
        []]

# Имя входного файла или директория
dir = sys.argv[-1]
# Чтение файлов
for i,file in enumerate(os.listdir(dir)):
    with open(os.path.join(dir,file), 'r', encoding='utf-8') as f:
        for line in f:
            data[i].append(float(line.strip()))
# Находим период с самым большим числом посетителей
for i in range(0,16):
    for j in range(1,5):
        data[0][i]+=data[j][i]
max = 0
fIndex = 0
for i in range(0,16):
    if data[0][i]>max:
        max = data[0][i]
        fIndex = i
print(fIndex+1)