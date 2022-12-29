a=int(input())
b=[]
c=0
d=1
b.append(c)
b.append(d)
for i in range(1,21):
    b.append(b[i]+b[i-1])
print(b[a])