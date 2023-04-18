# s=input("enter string")
# for i in range(0,len(s)):
#     if(ord(s[i])<92):
#         print(chr(i+32))
#     elif(ord(s[i])>97):
#         print(chr(i-32))
x=input()
for i in x:
    if i>='a' and i<='z':
        print(chr(ord(i)-32),end="")
    else:
        print(chr(ord(i)+32),end="")
        
    