x=int(input())
a=input(" ")
a=list(a.split(' '))
s={}
for i in a:
   if i in s:
      s[i]+=1
   else:
      s[i]=1
for key,value in s.items():
  if value==1:
     print(key)
      
