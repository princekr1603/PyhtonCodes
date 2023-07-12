#perfect no.=sum of factor of any no.is equal to no.
#ex- 6-1,2,3 then 1+2+3=6

n=int(input("enter no."))
sum=0
for i in range(1,n):
    if(n%i==0):
        sum=sum+i
if(sum==n):
    print(n,"is perfect no.")
else:
    print(n,"is not perfect no.")