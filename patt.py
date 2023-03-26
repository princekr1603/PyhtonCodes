x=int(input("enter no."))
# for i in range(-1,x):
#     print(" "*(1+i),end="")
#     print("* "*(x-1-i))
for k in range(-1,x):
    print(" "*(x-k),end="") 
    print("* "*(k))  
for i in range(-1,x):
    print(" "*(1+i),end="")
    print("* "*(x-1-i))