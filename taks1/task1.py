import numpy as np
import sys

input_list = []

# Имя входного файла или директория
file = sys.argv[-1]
# Чтение файла
with open(file, 'r', encoding='utf-8') as f:
    for line in f:
        input_list.append(int(line.strip()))

work_list = np.array(sorted(input_list))
# Перcентиль
print('%.2f' % round(np.percentile(work_list,90),2))
# Медиана
if len(work_list)%2==1:
    # Если длинна списка не четная, то медиана центральный элемент
    mid = (len(work_list)//2)+1
    print('%.2f' % round(work_list[mid],2))
else:
    # Если длинна списка четная, то медиана среднее от суммы центральных элементов
    left_mid = work_list[len(work_list)//2]
    right_mid = work_list[(len(work_list)//2)+1]
    print('%.2f' % round((left_mid+right_mid)/2,2))
# Максимальное значение
print('%.2f' % round(work_list[-1],2))
# Минимальное значение
print('%.2f' % round(work_list[0],2))
# Среднее значение
print('%.2f' % round(sum(work_list)/len(work_list),2))


