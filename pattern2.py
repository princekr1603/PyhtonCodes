n=int(input("enter no."))
for i in range(n+1):
    print(" "*(n-i),end="")
    print("* "*(i),end="")
    print(" "*2*(n-i),end="")
    print("* "*(i))
    