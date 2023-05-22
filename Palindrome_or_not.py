b=input()
a=b.lower()
t=-1
c=0
for i in range(len(a)):
    if a[i]==a[t]:
        c=c+1
        t=t-1 
    else:
        print("False")
        break
    if c==len(a):print("True")