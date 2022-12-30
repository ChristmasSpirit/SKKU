a=int(input())
while a!=-1:
    b=0
    c=[]
    d=0
    for i in range(1,a//2+1):
        if a%i==0:
            b+=i
            c.append(i)

    print(c)
    if b==a:
        def d():
            for i in c:
                print(i, end=' ')
        print(a,'=',d())
    a=int(input())
