n=int(input())
l=list(map(int,input().split()))
c=0
for i in range(len(l)):
    if l[i]==0 or l[i]==1:
        c+=1
if c==n:
    print("True")
else:
    print("False")