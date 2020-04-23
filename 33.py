# Заданий масив А (1:20). Знайти добуток всіх його ненульових елементів.
#licherep Artem
counter = 0
a = []
for i in range(5):
    a.append(int(input("input: ")))
for i in range(5):
    if a[i] > 0  or a[i]<0:
        counter += a[i]
print(counter)
