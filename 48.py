#Наведено список прізвищ брокерів товарної біржі з N чоловік. Поміняйте
#місцями прізвища брокерів: першого і останнього, другого і передостаннього, третього
#з початку і третього від кінця і т.д.
#licherep Artem

a=['ВАСА','ЛЕНА','ІВАН','ПЕТРО','КАРПОВИЧ','НАДІЯ','СЕРГІЇВНА']
c=list()#Новий масив в якому вимірюємо довжину масиву
for b in range(len(a)-1,-1,-1):#виходить що ми просто робимо в іншу сторону
    c.append(a[b])#добавляємо елементи в новий масив
print(c)