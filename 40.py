# Обчислити суму парних елементів одновимірного масиву до першого
# зустрінутого нульового елемента.
#licherep Artem
a = []
c = 0
b = 0
for i in range(5):
    a.append(int(input("input: ")))
for i in range(5):
    if a[i] == 0:
        break

for i in range(5):
    if a[i] == 0:
        c = a[: i]
        break
print(c)
for i in range(len(c)):
    if c[i] % 2 == 0:
        b = b + c[i]
print(b)
