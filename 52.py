#. Знайти найбільший елемент з елементів одновимірного масиву, що мають
#парний номер. Визначити, чи є він єдиним.
#licherep Artem
import numpy as np
import random


c=[]
counter=0
a = np.zeros(10, dtype=int)
for i in range(10):
    a[i] = random.randint(-5, 100)
print(a)

for i in range(len(a)):
    if a[i] not in c:
        counter += 1
        c.append(a[i])
print(counter)
