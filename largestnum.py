x=int(input())
y=input("")
z=list(y.split(""))
z.sort(reverse=True)
m=list(map(int,z))
if s(m)==0:
  print("0")
else:
  k="".join(z)
  print(k)
