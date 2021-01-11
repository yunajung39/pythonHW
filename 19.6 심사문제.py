a=int(input())

for i in range(a):
    for j in reversed(range(a)):
        if j > i:
            print(' ', end='')
        else:
            print('*', end='')
    for j in range(a):
        if j < i:
            print('*', end='')
    print()
