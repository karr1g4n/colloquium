# Знайти кількість парних елементів одновимірного масиву до першого
# зустрінутого числа рівного наперед заданому числу а.
#licherep Artem
import random
import numpy as np

b = int(input())
counter = 0
a=[1,2,3,4,5,6,7,8,9,0,1]
s = 0
for i in range(12):
    if a[i] == b:
        s = a[:i]
        break
print(s)
for j in range(len(s)):
    if a[j] % 2 == 0:
        counter += 1
print(counter)
