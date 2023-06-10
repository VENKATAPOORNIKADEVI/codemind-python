s=input()
a=0
for i in range(len(s)):
    if s[i]>='0' and s[i]<='9':
        a+=int(s[i])
print(a)