person=int(input())
object=[]
height=[]
for i in range(person):
    a,b=map(int,input().split())
    object.append((a,b))

for i in range(person):
    count = 0
    for j in range(person):
        if object[i][0]<object[j][0] and object[i][1]<object[j][1]:
            count+=1
    height.append(count+1)
for i in range(person):
    print(height[i],end=' ')
