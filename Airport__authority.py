n=int(input())
l=[]
c=0
for i in range(n):
    l.append(int(input()))
h=int(input())
for i in l:
    if i>h:
        c+=2
    elif i<=h:
        c+=1
print(c)
    