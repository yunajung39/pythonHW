import random
a=random.randint(1,100)

while True:
    b=int(input('숫자를 입력하시오 : '))
    if b>a:
        print("DOWN")
    elif b<a:
        print('UP')
    elif b==a:
        print('RIGHT')
        break