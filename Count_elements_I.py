a,b=map(int,input().split())
x=list(map(int,input().split()))
y=list(map(int,input().split()))
c=set(x)
d=set(y)
t=0
for i in c:
    for j in d:
        if i==j:
            t+=1
print(t)
