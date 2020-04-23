#Обчислити середнє арифметичне значення тих елементів одновимірного
#масиву, які розташовані за першим по порядку мінімальним елементом.
#licherep Artem
import numpy as np
a = np.array((23,11,322,79,45,63,7,52,645,756,999))
seredne = 0
min_index = 0
for i in range(len(a)):
    if a[i] == min(a):
        min_index = i
for j in range(min_index):
    seredne += a[j]
print('Середнє арифметичне =',seredne/min_index)