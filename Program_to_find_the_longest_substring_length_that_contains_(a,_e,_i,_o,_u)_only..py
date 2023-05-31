n=input()
c=0
x=0
for i in n:
    if i in "aeiou":
        c+=1
        x=max(c,x)
    else:
        c=0
print(x)