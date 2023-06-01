n=input()
c=0
co=0
b='aeiou'
d='AEIOU'
for i in b:
    if i in n:
        c+=1
for i in d:
    if i in n:
        co+=1
if(c==5 or co==5):
    print('True')
else:
    print('False')