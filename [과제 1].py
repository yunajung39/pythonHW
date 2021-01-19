with open('article.txt', 'r', encoding='UTF8')as x:
    x=x.read()
    x=x.replace('”','')
    x=x.replace(',','')
    x=x.replace("’",'')
    x=x.replace('.','')
    x=x.replace('-','')
    x=x.replace('“','')
    x=x.replace('\n','')     #문자대체
    x=x.lower()         #소문자
    x=x.split()      #단어들로만 리스트 만들기

b={} #어떤단어 몇개인지 딕셔너리로
c=0
for i in x:
    for i in x:
        if i==x[0]:
            c+=1
            b[i]=c
            del i
        elif i is x[-1]:
            c=0
            del x[0]
        
b=sorted(b.items(), key=lambda y: y[1], reverse=True)
print(b[:3])