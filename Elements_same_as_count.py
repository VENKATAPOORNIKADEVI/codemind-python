a=int(input())
b=list(map(int,input().split()))
c=[]
v=0
for i in range(a):
    if b.count(b[i])==b[i]:
        c.append(b[i])
m = list(dict.fromkeys(c))
for i in range(len(m)):
    print(m[i],end=" ")
if len(m)==0:
    print(-1)