# Дано два лінійних масиву однакової розмірності. Скласти третій масив з
# добутку елементів перших двох масивів, що стоять на місцях з однаковим індексом.
#licherep Artem
import random
import numpy as np
a=np.zeros(10,dtype=int)
b=np.zeros(10,dtype=int)
c=np.zeros(10,dtype=int)
for i in range(0,10,1):
    (a[i])=random.randint(-5,5)
print(a)
for i in range(0,10,1):
    (b[i])=random.randint(-5,5)
print(b)
for i in range(len(a)):
    for i in range(len(b)):
        for i in range(len(c)):
            c[i]=a[i]*b[i]
print(c)
