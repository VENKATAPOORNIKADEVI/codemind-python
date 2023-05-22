b=list(map(str,input().split()))
v=0
for i in range(len(b)):
    a=b[i].lower()
    t=-1
    c=0
    for j in range(len(a)):
        if a[j]==a[t]:
            c=c+1
            t=t-1
        else:break
    if c==len(a):v=v+1
print(v)