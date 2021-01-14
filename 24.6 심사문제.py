a=input().split(';')
a=list(map(int,a))
a.sort(reverse=True)

for i in a :
    print('%9s' % format(i, ','))