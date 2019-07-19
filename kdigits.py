from itertools import combinations
s,u=map(int,input().split())
l1=len(str(s))
l2=list(combinations(str(s),l1-u))
l2=sorted(l2)
print(*l2[0],sep=' ')
