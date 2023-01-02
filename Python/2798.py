import sys
input=sys.stdin.readline
a,b=map(int,input().split())
c=list(map(int,input().split()))
c=sorted(c)
d=[]
for i in range(a):
    for j in range(i+1,a):
        for k in range(j+1,a):
            if c[i]+c[j]+c[k]<=b:
                d.append(c[i]+c[j]+c[k])
print(max(d))
