x=int(input())
y=list(map(int,input().split()[:x]))
z=sorted(y)
for i in z:
  print(i,end=' ')
