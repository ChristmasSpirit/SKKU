a=int(input())
b=int(input())
c=[]
for i in range(1,101):
    i=i*i
    c.append(i)
d=0
e=[]
for i in c:
    if a<=i and b>=i:
        d+=i
        e.append(i)
if d>0:
    print(d)
    print(e[0])
else:
    print('-1')

