a=int(input())
b=int(input())
d=0
for i in range(a):
    c=list(map(int,input().split()))
    d+=sum(c)
print(d)  
  