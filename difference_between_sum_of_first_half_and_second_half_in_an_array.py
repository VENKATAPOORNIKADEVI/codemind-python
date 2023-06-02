n=int(input())
l=list(map(int,input().split()))
a=0
b=0
for i in range(0,n//2):
    a+=l[i]
for i in range(n//2,n):
    b+=l[i]
print(abs(a-b))