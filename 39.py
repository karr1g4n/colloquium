# Дані про температуру повітря і кількості опадів за декаду квітня
# зберігаються в масивах. Визначити кількість опадів, що випали у вигляді дощу і у
# вигляді снігу за цю декаду.
#licherep Artem
import numpy as np
import random

conter = 0
conter_2 = 0
a = []
b = []
for i in range(2):
    a.append(int(input('введіть скілки опадів випало у вигляді дощю  ', )))
print(a)
for i in range(2):
    b.append(int(input('введіть скілки опадів випало у вигляді снігу  ')))

for i in range(2):
    conter += a[i]
    for j in range(2):
        conter_2 += a[j]
print("дощю",conter)
print("снігу",conter_2)