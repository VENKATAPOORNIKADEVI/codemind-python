a=int(input())
b=list(map(int,input().split()))
e=0
o=0
for i in range(len(b)):
    if i%2==0:
        e+=b[i]
    else:
        o+=b[i]
if e>o:
    print(e-o)
else:
    print(o-e)