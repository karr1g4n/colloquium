# Задано два натуральних числа a і b. Змінній w привласнити значення
# істина, якщо в одновимірному цілочисельному масиві є хоча б один елемент, кратний а
# і не кратний b.
#licherep Artem
import numpy as np
import random

w = False

a = int(input("input: "))
b = int(input("input: "))
counter = 0
b = np.zeros(5, dtype=int)
for i in range(5):
    b[i] = random.randint(-5, 100)
print(a)
for i in range(5):
    if b[i] % a == 0 and b[i] % b != 0:
        w = True
print(w)
