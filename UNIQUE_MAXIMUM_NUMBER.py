n=int(input())
a=list(map(int,input().split()))
u=[]
for i in a:
    if a.count(i)==1:
        u.append(i)
if len(u)==0:
    print(-1)
else:
    print(max(u))
