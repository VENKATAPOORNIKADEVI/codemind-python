s=input()
m=int(input())
n=int(input())
l = len(s)
for i in range(0,l):
    if i>=m and i<=n:
        print(s[i],end="")