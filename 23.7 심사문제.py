a, b=map(int,input().split())
matrix = []
for i in range(b):
    matrix.append(list(input())) #지뢰판만들어짐

for c in range(a):
    for d in range(b):
        if matrix[c][d]=='*':
            print('*',sep='', end='') #지뢰에는지뢰표시
        else:
            e=0
            for f in range(-1,2):
                for g in range(-1,2): #자기 기준 3x3 읽기
                    if 0<=c+f<b and 0<=d+g<a and \
                    matrix[c+f][d+g]=='*':  #3x3이 지뢰판 범위인지 체크, 요소가 지뢰인지 체크
                        e+=1             #3x3중에 지뢰있으면 +1
            print(e,sep='',end='')     #지뢰갯수표시
    print()