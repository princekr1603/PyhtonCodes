str=input("enter string")
count=0
for i in range(0,len(str)):
    for j in str:
        if(j==str[i]):
            n=j
            count=count+1        
    if(count>0):
        print(n," ",count)
    count=0  