a=input()
x=input()
ct=0
for i in a:
    if(i==x):
        ct+=1
if(ct>0):
    print(ct)
else:
    print('-1')