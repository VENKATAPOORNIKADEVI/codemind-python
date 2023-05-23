n=int(input())
l=list(map(int,input().split()))
c=0
avg=sum(l)//n
for i in range(n):
    if l[i]>=avg:
        c+=1
print(c)