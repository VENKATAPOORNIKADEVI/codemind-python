s=input()
v='aeiou'
c=0
m=0
for i in range(len(s)):
    if s[i] in v:
        c+=1
        m=max(m,c)
    else:
        c=0
print(m)