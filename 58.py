#Дан одновимірний масив цілих чисел. Знайдіть, скільки разів в ньому
#повторюється найчастіше число.
#licherep Artem
import collections
import numpy as np
a = np.array(())
while True:
    inp = input()
    if not inp:
        break
    a = np.append(a, inp)
count = collections.Counter.most_common(collections.Counter(a))[0]
print('Найчастіше число', count[0], 'повторяється:', count[1])