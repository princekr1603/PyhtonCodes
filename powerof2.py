# n=int(input("enter no."))
# while(n%2==0):
#     n=n//2
# if(n==1):
#     print("power of 2")
# else:
#     print("not power of 2")


#method2---recursion

def checkr(n):
    if (n==0 or n%2!=0):
        return False
    if(n==1):
        return True
    return checkr(n//2)

n=int(input("enter no."))
print(checkr(n))





