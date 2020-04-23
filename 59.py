#Дан одновимірний масив з 10 цілих чисел. Підрахуйте кількість різних
#чисел в ньому.
#licherep Artem 
import collections
import numpy as np
a = np.array(())
while True:
    inp = input()
    if not inp:
        break
    a = np.append(a, inp)
count = collections.Counter.most_common(collections.Counter(a))
print(len(count))