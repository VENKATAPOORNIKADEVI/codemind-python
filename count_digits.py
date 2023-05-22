n=int(input())
a=list(map(int,input().split()))
for i in a:
    s=str(i)
    p=len(s)
    if i<0:
        p-=1
    print(p,end=" ")