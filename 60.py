# Дан одновимірний масив з 10 цілих чисел. Підрахуйте найбільше число
# однакових чисел, що йдуть підряд
#licherep Artem
a = []
b=[]
count = 0
for i in range(10):
    a.append(int(input("input:")))
print(a)
for i in range(10):
    if a[i] == a[i - 1]:
        count += 1
        b.append(count)
print('число однакових чисел,що йдут пыдряд:', max(b))