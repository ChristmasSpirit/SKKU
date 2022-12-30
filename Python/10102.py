a=int(input())
d=0
e=0
for i in range(a):
    b=int(input())
    if b==1:
        e+=1
    else:
        d+=1
print(d,e)
if d>e:
    print("Junhee is not cute!")
else:
    print("Junhee is cute!")