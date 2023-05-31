a,b=map(int,input().split())
x=list(map(int,input().split()))
y=list(map(int,input().split()))
c=set(x)
d=set(y)
m=0
n=0
for i in c:
    if i not in d:
        m+=1
for j in d:
    if j not in c:
        n+=1
print(m+n)