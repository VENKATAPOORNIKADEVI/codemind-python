n=int(input())
l=list(map(int,input().split()))
a=int(input())
s=0
for i in l:
    if i<=a:
        s+=i
print(s)