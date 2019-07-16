x=int(input())
a=input("")
a=list(a.split(" "))
l=[]
for i in range(0,len(a)):
   for j in range(i+1,len(a)):
      if a[i]==a[j]:
        l.append(a[i])
if(len(l)==0):
   print("uniqye")
else:
   print(l[0])
