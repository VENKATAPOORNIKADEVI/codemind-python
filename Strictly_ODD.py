n=int(input())
a=list(map(int,input().split()))
for i in range(n):
    if a[i]%2==1:
        if i%2==0:
            print(False)
            break
else:
    print(True)