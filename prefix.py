l1=int(input())
k=[]
for i in range(0,l1):
   k.append(input())
l1=len(k[0])
s=""
for i in range(0,l1):
   c=k[0][i]
   f=0
   for j in range(0,l1):
        if(c!=k[j][i]):
           f=1
   if(f==0):
     s=s+c
   else:
     break
print(s)
