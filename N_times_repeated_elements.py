a=int(input())
b=list(map(int,input().split()))
d=int(input())
c=[]
v=0
for i in range(a):
    if b.count(b[i])==d:
        c.append(b[i])
m = list(dict.fromkeys(c))
if len(m)==0:
    print(-1)
for i in range(len(m)):
    print(m[i],end=" ")