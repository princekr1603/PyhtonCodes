n=int(input("enter no:"))
for i in range(1,n+4):
    if(i<n):
        print(" "*(n-i),end="")
        print("*"*(2*i-1))
    else:
        print(" "*(n-1),end="")
        print("*")