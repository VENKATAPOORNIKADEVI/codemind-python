n=input()
s=n.split()
c=[]
for i in range(len(s)):
    k=s[i]
    c1=ord(min(k))
    c2=ord(max(k))
    c.append(abs(c1-c2))
print(*c)