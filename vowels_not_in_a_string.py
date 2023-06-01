n=input()
c=0
b='aeiou'
for i in b:
    if i not in n:
        c+=1
        print(i,end=' ')
if(c==0):
    print('0')