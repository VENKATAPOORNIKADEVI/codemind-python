n=int(input())
a=list(map(int,input().split()))
b=[]
for i in a:
    i=str(i)
    b+=[len(i)]
print(b.count(max(b)))