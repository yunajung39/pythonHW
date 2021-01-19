a=list(range(1,10001))
b=set()

for i in range(10000) :
    x=a[i]
    y=x//1000
    z=x%1000//100
    w=x%1000%100//10
    v=x%1000%100%10
    b.add(x+y+z+w+v)
a=set(a)
c=a-b

for i in sorted(c):
    print(i)
