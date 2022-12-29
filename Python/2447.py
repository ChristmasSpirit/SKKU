a=int(input())
b=0
while a!=1:
    a=a//3
    b=b+1
for i in range(a):
    if a//3!=0 and i//(a//3)==1:
        print('*'*(a//3),' '*(a//2),'*'*(a))