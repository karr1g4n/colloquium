# З 8 до 20 години температура повітря вимірювалася щогодини. Відомо,
# що протягом цього часу температура знижувалася. Визначте, о котрій годині було
# вперше зафіксовано від'ємну температуру.
#licherep Artem
import numpy as np


a = []
for i in range(3):
    b = []
    b.append(int(input("input: ")))
    a.append(b)
print(a)
array = np.array(a)
c = []
time=0
for i in range(0,3,1):
    if array[i] < 0:
        time=i+8
        c = array[i]
        break
print("температура -", c)
print("час захыксування-", time)