st=input()
s=[]
for i in st:
    if i in 'aeiouAEIOU':
        if i not in s:
            s.append(i)
print(*s)       