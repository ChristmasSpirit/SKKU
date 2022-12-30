def maker(n):
  c=maker(n//3)
  b=[]
  for star in c:
    b.append(star*3)
  for star in c:
    b.append(star+' '*(n//3)+star)
  for star in c:
    b.append(star*3)
  return b
a=int(input())
if a==1:
    print('*')
else:
    print('\n'.join(maker(a)))
