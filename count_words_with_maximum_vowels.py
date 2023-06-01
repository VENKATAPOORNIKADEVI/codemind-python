l=list(map(str,input().split()))
arr=[]
if len(l)==1:
    c=0
    for r in l[0]:
        if r in 'aeiouAEIOU':
            c=1
    print(c)
else:
    for h in l:
        c=0
        for r in h:
            if r in 'aeiouAEIOU':
                c+=1
        arr.append(c)
    c=0
    for i in range(len(arr)):
        if arr[i]==max(arr):
            c+=1
    print(c)
