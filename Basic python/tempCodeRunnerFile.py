n=int(input("enter no:"))
a=0
for i in range(1,n+1):
    for j in range(1,i+1): 
        print(a+(n-i-j+4),end=" ")
    a+=1
    print(" ")