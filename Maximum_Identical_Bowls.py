def bowl(l,s,n):
    for i in range(n,0,-1):
        if(s%i==0):
            return i
    else:
        return 0

n=int(input())
l=list(map(int,input().split()))
s=sum(l)
print(bowl(l,s,n))