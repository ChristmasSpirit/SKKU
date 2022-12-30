import sys
input=sys.stdin.readline
a=int(input())
for i in range(a):
    b=int(input())
    e={}
    f=[]
    for i in range(b):
        c,d=map(str,input().split())
        d=int(d)
        e[d]=c
        f.append(d)
    d=max(f)
    print(e[d])
