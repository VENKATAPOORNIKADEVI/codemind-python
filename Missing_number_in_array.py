def Missing(a):
    n=len(a)
    t = (n + 1)*(n + 2)/2
    s= sum(a)
    return t-s
n=int(input())
for i in range(n):
    x=int(input())
    a=list(map(int,input().split()))
    print(int(Missing(a)))