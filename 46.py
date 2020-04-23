#Задана таблиця назв товарів, що випускаються заводом. Визначте, чи
#повторюється в цій таблиці назва першого товару, і, якщо повторюється, видаліть
#назву першого товару з таблиці.
#licherep Artem
import collections
import numpy as np
a = np.array(())
while True:
    inp = input()
    if not inp:
        break
    a = np.append(a, inp)
count = collections.Counter(a)
if count[a[0]] > 1:
    a = np.delete(a, 0)
print(a)