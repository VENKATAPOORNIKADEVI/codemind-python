a=input()
a.lower()
s=input()
for i in range(len(a)):
    if a[i]==s:
        print("True")
        print(i)
        break
else:
    print("False")