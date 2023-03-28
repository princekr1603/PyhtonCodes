x=int(input("enter no."))
ans=0
while(x!=0):
    y=x%10
    x=x//10
    ans=ans+y
print(ans)