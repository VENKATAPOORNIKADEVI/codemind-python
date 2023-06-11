a=int(input())
b=list(map(int,input().split()))
s = [str(i) for i in b]
bi = int("".join(s))
d=0
i = 0
while(bi != 0):
    dec = bi % 10
    d = d + dec * pow(2, i)
    bi = bi//10
    i += 1
print(d)