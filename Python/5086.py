a,b=map(int,input().split())
while a!=0 and b!=0:
    if a/b==a//b:
        print('multiple')
    elif b/a==b//a:
        print('factor')
    else:
        print('neither')
    a, b = map(int, input().split())
