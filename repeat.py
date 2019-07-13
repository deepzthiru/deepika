l=[]
l1=[]
s=""
x=input()
if(x>=1 and x<=100000):
  for i in range(0,x):
  l.append(input("Enter  a number"))
  for i in range(0,x):
    for j in range(i+1,x):
      if(l[i]==l[j]):
       # print(l[i],end=('')
       l1=l[i]
      else:
        print("unique")
l1.sort()
for i in l1:
   s+=" "+str(i)
