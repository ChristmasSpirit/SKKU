a,b=map(int,input().split())
c=[]
g=[]
for i in range(a):
    c.append(input())
for i in range(a-7):
    for j in range(b-7):
        d=0
        e=0
        for l in range(i,i+8):
            for k in range(j,j+8):
                if (l+k)%2!=0:
                    if c[l][k]=='W':
                        d+=1
                    elif c[l][k]=='B':
                        e+=1
                else:
                    if c[l][k]=='B':
                        d+=1
                    elif c[l][k]=='W':
                        e+=1

        g.append(min(d,e))
print(min(g))

