a=int(input())
def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a
for i in range(a):
    b,c=map(int,input().split())
    d=b*c/gcd(b,c)
    print(int(d))






