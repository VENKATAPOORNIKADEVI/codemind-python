n=int(input())
l=list(map(int,input().split()))
if(len(set(l))==1):
    print("0")
else:
    c=0
    eq=0
    for i in range(n):
        c=0
        for j in range(i,n):
            if(l[i]==l[j]):
                c+=1
                if(eq<c):
                    eq=c
    print(eq)
