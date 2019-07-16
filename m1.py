n=int(input())
l=[int(i) for i in input().split()]
l1=[]
for i in range(0,len(l)):
  if i==l[i]:
    l1.append(l[i])
  if len(l1)==0:
     print("-1")
  else:
    for x in range(len(l1)):
       print(l1[x],end=" ")
