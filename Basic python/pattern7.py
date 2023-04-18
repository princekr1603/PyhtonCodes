n=int(input("enter no:"))
a=0
b=0
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i+a+b,end=" ")
        a=a+i
        b=a-b+j    
    print()