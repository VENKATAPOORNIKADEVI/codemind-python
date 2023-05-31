a,b=map(int,input().split())
c=list(map(int,input().split()))
d=list(map(int,input().split()))
e=[]
f=[]
for i in c:
    if i not in e:
        e.append(i)
for i in d:
    if i not in f:
        f.append(i)
for i in e:
    if i not in f:
        print(i,end=" ")
for i in f:
    if i not in e:
        print(i,end=" ")