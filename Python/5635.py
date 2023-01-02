a,b=map(int,input().split())
c=[]
d=[]
for i in range(a):
    c.append(input())
for i in range(b):
    d.append(input())
e=0
for i in d:
    if i in c:
        e+=1
print(e)

