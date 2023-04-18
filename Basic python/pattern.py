n= int(input("enter no."))

for i in range(1,n+1):
    a=90
    for j in range(1,i+1):
        print(chr(a) ,end="")
        a-=2    
    print()