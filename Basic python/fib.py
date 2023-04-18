n=input("enter no")
s=""
for i in range(len(n)):
    if(i==1 or i==len(n)-2):
        s+=chr(ord(n[i])-32)
    else:
        s+=n[i]
print(s)
    