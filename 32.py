# Змінній t привласнити значення істина, якщо в одновимірному масиві є
# хоча б одне від’ємне і парне число.
#licherep Artem
t = False
c = 0
c_2 = 0
a = [-1, 2, 3, 4]
for i in range(len(a)):
    if a[i] < 0:
        c = 1
        break
print(c)
for i in range(len(a)):
    if a[i] % 2 == 0:
        c_2 = 1
print(c_2)
if c == 1 and c_2 == 1:
    t = True
print(t)
