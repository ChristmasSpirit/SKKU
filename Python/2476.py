a=int(input())
g=[]
for i in range(a):
    e=b,c,d=list(map(int,input().split()))
    e=sorted(set(e))
    if len(e)==3:
        g.append(max(e)*100)
    elif len(e)==2:
        if b==c:
            g.append(1000+100*b)

        elif b == d:
            g.append(1000+100*b)

        elif c == d:
            g.append(1000+100*d)
    elif len(e)==1:
        g.append(10000+1000*b)
g=sorted(g)
print(g[a-1])
