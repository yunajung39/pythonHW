x=input()
x=x.replace('-','')
x=x.replace(',','')
x=x.replace("'",'')
x=x.replace('.','')
x=x.replace('\n','')
x=x.split()

c=0
for i in x:
    if i=='the':
        c+=1
        
print(c)