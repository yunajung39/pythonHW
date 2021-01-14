with open('words.txt', 'r')as x:
    x=x.read()
    y=x.split('\n')

for i in y:
    if i==i[::-1]:
        print(i)