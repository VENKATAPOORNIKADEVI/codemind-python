n=int(input())
c=[]
l=list(map(int,input().split()))
a,b=map(int,input().split())
for i in range(len(l)):
    if(a<=l[i] and l[i]<=b):
        c.append(l[i])
if(len(c)>=2):
    print(min(c))
else:
    print(-1)