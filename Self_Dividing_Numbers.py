def self(n):
    c=0
    t=0
    k=n 
    while(n!=0):
        o=n%10
        c=c+1
        if o!=0:
            if k%o==0:
                t=t+1
        n=n//10
    if(c==t):
       return True
    else: 
       return False
e=int(input())
s=int(input())
for i in range(e,s+1):
    if self(i):
        print(i,end=" ")