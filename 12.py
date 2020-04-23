# Дані про температуру повітря за декаду грудня зберігаються в масиві.
# Визначити, скільки раз температура була вище середньої за цю декаду.
#licherep Artem
a = []

for i in range(30):
    a.append(int(input("input: ")))
print(a)
counter = 0
for i in range(30):
    if a[i] > -4 :
        counter += 1
print("стільки разів температура була вище середньої за цю декаду: ",counter)