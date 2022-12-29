a=int(input())
b=1
if a!=0:
    for i in range(1,a+1):
        b*=i
else:
    b=1
print(b)