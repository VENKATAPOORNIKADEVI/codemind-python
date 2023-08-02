s= int(input())
st = input() 
flag = st.find("HH") 
if flag == -1:
    print("YES") 
    print(st.replace(".","B")) 
else:
    print("NO")