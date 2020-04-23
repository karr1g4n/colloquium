#У лотереї розігрувалося 100 квитків. Таблиця містить 10 номерів
#виграшних квитків. Перевірте, чи є квиток з номером N виграшним.
#licherep Artem
import collections
import random
import numpy as np
tickets = np.arange(100)
win = np.array(())
k = 0
N = int(input('Введіть номер квитка'))
while k != 100:
    x = random.choice(tickets)
    if x not in win:
        win = np.append(win, x)
        k += 1
if N in win:
    print('Ваш квиток є виграшним!')
else:
    print('Ваш квиток не є виграшним')
print('Виграшні номери:',win)