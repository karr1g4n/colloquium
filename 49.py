#Задано дві таблиці. Одна містить найменування послуг, а інша - розцінки
#за ці послуги. Видаліть з обох таблиць все, що передує послузі, ціна якої G гривень.
#licherep Artem
a=['aaa','bbb','ccc','ddd']#1 масив
b=[14,1645,456345,45365634563456]#2 масив
c=int(input())#ціна товару який потрібно видалити
for d in range(len(b)):#діапазон
    try:
        if b[d]==c:
            a.remove(a[d])
            b.remove(b[d])
    except:
        break
print(a)
print(b)