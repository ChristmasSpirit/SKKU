a=int(input())
b=[]
for i in range(a):
    b.append(list(map(int,input().split())))
for i in range(a):
    if b[i][1]==max(b):
        b[i][1]=1

