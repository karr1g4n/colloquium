#Підрахувати кількість елементів одновимірного масиву, для яких
#виконується нерівність i*i<ai<i!
#licherep Artem
import math
e=0
for a in range(10):#діапазон
    c=math.factorial(a)# факторіал іерції
    d=a*a#квадртат ітерації
    b=int(input())
    print(f'{c} меньше ніж це')
    print(f'{d} больше ніж це')
    if d<b<c:#умова
        e+=1#лічильник
print(e)