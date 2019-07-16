n=list(map(str,input()))
set1=cs=0
for i in range(0,len(n)-1):
  q=n[i]
  if int(q)!=0:
    for i in range(i+1,i+2):
      q=q+n[i]
      if int(q)<27 and int(q)>0:
         set1=set1+1
      elif int(q)==0:
         set1=set1-1
      else:
         break
if set1!=1:
   cs=set1%2
print(set1+cs+1)
