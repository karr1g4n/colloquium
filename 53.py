
#В масиві X (1: n) кожен елемент рівний 0, 1 або 5. Переставити елементи
#масиву так, щоб спочатку розташовувалися всі нулі, потім все одиниці, а потім всі
#п'ятірки. Додаткового масиву не заводити.
#licherep Artem
#за сотріровкою selection
a=[0,1,5,0,1,5,0,1,5]
for b in range(len(a)-1):
    c=b
    for d in range(b+1,len(a)):
        if a[d]<a[c]:#шукаємо мінімальний елемент з остатків і ставимо його в початок
            c=d
    a[b],a[c]=a[c],a[b]
print(a)