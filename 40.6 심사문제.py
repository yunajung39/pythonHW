def prime_number_generator(start,stop):
    for j in range(start, stop):
        a=True
        for i in range(2, int((j**0.5)+1)):
            if j%i==0:
                a=False
                break
        if a==True:
            yield j

start, stop = map(int, input().split())
 
g = prime_number_generator(start, stop)
print(type(g))
for i in g:
    print(i, end=' ')