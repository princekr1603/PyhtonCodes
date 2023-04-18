n=input("enter string:")
lower=0
upper=0
for i in n:
    if((i>='a'and i<='z')):
        lower+=1
        
    if(i>='A' and i<='Z'):
        upper+=1
        
print("lower case =",lower)
print("upper case=",upper)
