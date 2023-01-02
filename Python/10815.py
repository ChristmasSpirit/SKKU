import sys
input=sys.stdin.readline
a=int(input())
b=list(input().split())
c=int(input())
d=list(input().split())
e={}
for i in range(a):
    e[b[i]]=0
for i in range(c):
    if d[i] in e:
        print(1,end=' ')
    else:
        print(0,end=' ')