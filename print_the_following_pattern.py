n=int(input())
for i in range(n):
    for j in range(n-(i+1)):
        print(" ",end="")
    for j in range(i+1):
        print(i+1,end="")
    for j in range(i):
        print(i+1,end="")
    print("")