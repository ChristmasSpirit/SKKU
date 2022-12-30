a=input()
b=[]
c=0
for i in a:
    b.append(i)
for i in range(len(b)//2):
    if b[i]==b[-1-i]:
        c+=1
if c==len(b)//2:
    print('1')
else:
    print('0')