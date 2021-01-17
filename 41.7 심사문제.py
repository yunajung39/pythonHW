def calculation(line):
    a=line.split(' ')
    a[0]=int(a[0])
    a[2]=int(a[2])
    if a[1]=='+':
        return a[0]+a[2]
    elif a[1]=='-':
        return a[0]-a[2]
    elif a[1]=='*':
        return a[0]*a[2]
    elif a[1]=='/':
        return a[0]/a[2]

def calc():
    result=False
    while True:
        line=(yield result)
        result=calculation(line)

expressions = input().split(', ')
 
c = calc()
next(c)
 
for e in expressions:
    print(c.send(e))
 
c.close()