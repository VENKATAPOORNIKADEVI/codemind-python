a=int(input())
b=list(map(int,input().split()))
c=[]
v=0
for i in range(a):
    if b.count(b[i])==b[i]:
        c.append(b[i])
m = list(dict.fromkeys(c))
if len(m)!=0:
    print(min(m),max(m))
else:
    print(-1)