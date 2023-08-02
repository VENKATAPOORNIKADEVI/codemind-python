a=input()
for i in range(len(a)-1,-1,-1):
    if(a[i]==' '):
        for j in range(i+1,len(a)):
            if(a[j]==' '):
                break
            print(a[j],end='')
        print(' ',end='')
for i in a:
    if(i!=' '):
        print(i,end='')
    else:
        break