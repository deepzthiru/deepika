l=[]
l1=[]
s=""
x=input()
for i in range(0,x):
  l.append(input("Enter  a number"))
for i in range(0,x):
  for j in range(i+1,x):
     if(l[i]==l[j]):
       # print(l[i],end=('')
       l1=l[i]
l1.sort()
for i in l1:
  s+=" "+str(i)
