import random
while True:
    a=random.randint(0,9)
    b=random.randint(0,9)
    c=random.randint(0,9)
    if a==b or a==c or b==c:
        continue
    else:
        break

while True:
    d, e, f=map(int,input('세 숫자를 띄어쓰기를 넣어 입력하시오 : ').split())
    g=0 #스트라이크
    h=0 #볼
    if a==d:
        g+=1
    if a==e:
        h+=1
    if a==f:
        h+=1
    if b==d:
        h+=1
    if b==e:
        g+=1
    if b==f:
        h+=1
    if c==d:
        h+=1
    if c==e:
        h+=1
    if c==f:
        g+=1
    if g==3:
        print('정답입니다! 정답 : ',a,b,c)
        break
    if g==0 and h==0 :
        print('OUT')
        continue
    print(g,'S',h,'B')
