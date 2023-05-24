st=input().split()
a=[]
for i in range(len(st)):
    if i%2==0:
        a.append(st[i][::-1])
    else:
        a.append(st[i])
print(*a)
