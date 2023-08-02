n=int(input())
for i in range(n):
    a=input()
    c=0
    for i in a:
        if i>='0' and i<='9':
            c+=1
    if c==len(a):
        print('True')
    else:
        print('False')