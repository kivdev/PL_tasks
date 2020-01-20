import sys
from collections import OrderedDict

data = []
times = set()

# Имя входного файла или директория
file = sys.argv[-1]
# Чтение файла
with open(file, 'r', encoding='utf-8') as f:
    for line in f:
        inp = line.split(' ')[0]
        out = line.split(' ')[1]
        # 8:30 -> 830
        inp = int((inp.split(':')[0] + inp.split(':')[1]).strip())
        out = int((out.split(':')[0] + out.split(':')[1]).strip())
        data.append((inp, out))
        times.add(inp)
        times.add(out)

data.sort(key=lambda x: x[0])
times = sorted(list(times))
in_bank = []
result = OrderedDict()
count = 0
max_count = 0
# Для каждого времени смотрим состояния клиентов
for i in times:
    for j in data:
        if j[1] < i:
            continue
        if j[0] == i:
            in_bank.append(j)
            count += 1
        if j[1] == i:
            in_bank.remove(j)
            count -= 1
        if max_count < count:
            start = j[0]
            max_count = count
        if max_count > count:
            if (start, i) not in result.keys():
                if result:
                    key = list(result.keys())[-1]
                    if key[1] == start and result[key] == max_count:
                        value = result.pop(key)
                        result.update({(key[0], i): value})
                    else:
                        result.update({(start, i): max_count})
                else:
                    result.update({(start, i): max_count})
            max_count = count
        if j[0] > i:
            break
max_values = []
max_val = 0
# Отбираем самые посещаемые промежутки
for i in list(result.keys()):
    if result[i] > max_val:
        max_values = []
        max_values.append(i)
        max_val = result[i]
    elif result[i] == max_val:
        max_values.append(i)
# Приводим к нормальному виду и выводим
for i in max_values:
    print(f'{str(i[0])[:-2]}:{str(i[0])[-2:]} {str(i[1])[:-2]}:{str(i[1])[-2:]}')
