# Обчислити середнє арифметичне значення тих елементів одновимірного
# масиву, які потрапляють в інтервал від -2 до 10.
#licherep Artem
import random
import numpy as np

s = 0
counter = 0
counter_2 = 0
a = np.zeros(10, dtype=int)
for i in range(10):
    a[i] = random.randint(10, 100)
print(a)
for i in range(10):
    if a[i] >= -2 and a[i] <= 10:
        counter += 1
        counter_2 += a[i]
        s = counter_2 / counter
print(s)
