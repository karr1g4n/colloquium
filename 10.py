# Дані про температуру повітря за декаду листопада зберігаються в масиві.
# Визначити, скільки разів температура опускалася нижче -10 градусів.
#licherep Artem
a = []

for i in range(30):
    a.append(int(input("input: ")))
print(a)
counter = 0
for i in range(30):
    if a[i] < 10:
        counter += 1
print("число разів скільки температура була нижче -10: ",counter)
