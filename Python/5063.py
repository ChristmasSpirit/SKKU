a=int(input())
for i in range(a):
    b,c,d=map(int,input().split())
    if b<c-d:
        print('advertise')
    elif b==c-d:
        print('does not matter')
    else:
        print('do not advertise')