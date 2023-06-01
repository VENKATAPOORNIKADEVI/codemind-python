s=input()
res=list()
top=-1
a=0
f=0
for i in range(len(s)):
    if s[i]=='{' or s[i]=='[' or s[i]=='(':
        top+=1
        res.append(s[i])
    else:
        if s[i]=='}' and top!=-1 and res[top]=='{':
            top-=1
            res.pop()
        elif s[i]==']' and top!=-1 and res[top]=='[':
            top-=1
            res.pop()
        elif s[i]==')' and top!=-1 and res[top]=='(':
            top-=1
            res.pop()
        else:
            a=i+1
            f=1
            break
if f==0 and top!=-1:
    a=i+2
print(a)           