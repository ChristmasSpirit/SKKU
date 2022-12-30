a=input()
b=[]
c=10
for i in a:
    b.append(i)
for i in range(1,len(b)):
    if b[i-1]=='(' and b[i]=='(':
        c+=5
    elif b[i-1]=='(' and b[i]==')':
        c+=10
    elif b[i-1]==')' and b[i]=='(':
        c+=10
    elif b[i-1]==')' and b[i]==')':
        c+=5
print(c)