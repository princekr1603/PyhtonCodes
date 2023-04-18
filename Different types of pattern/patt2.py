n=int(input("enter no."))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(""*(n-i),end="")
        if(i%2!=0):
            print(chr(64+i),end="")
        else:
            print(i,end="")
    print()