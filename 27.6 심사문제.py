with open('words.txt', 'r')as x:
    x=x.read()
    x=x.replace('-','')
    x=x.replace(',','')
    x=x.replace("'",'')
    x=x.replace('.','')
    x=x.replace('\n','')
    y=list(x.split())

    for z in y:
        if 'c' in z:
            print(z)
