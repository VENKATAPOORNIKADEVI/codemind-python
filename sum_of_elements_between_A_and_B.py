n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
m=0
c=0
for i in range(n):
    if l[i]>=a and l[i]<=b:
        m+=l[i]
print(m)