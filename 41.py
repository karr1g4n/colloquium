
#Змінній t привласнити значення істина, якщо максимальний елемент
#одновимірного масиву єдиний і не перевищує наперед заданого числа а.
#licherep Artem

t=False
a=int(input())
d=-999
e=list()
for b in range(10):
    c=int(input())
    if c>d:
        d=c
    e.append(c)
f=(e.count(d))
if f==1 and d<=a:
    t=True
    print(t)