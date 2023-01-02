a=int(input())
for i in range(a):
    e = []
    b = int(input())
    for i in range(b):
        c,d=map(str,input().split())
        c=int(c)
        e.append((c,d))
    e=sorted(e,key=lambda x: x[0])
    print(e[-1][1])