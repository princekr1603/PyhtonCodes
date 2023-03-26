x=int(input("enter no"))
# y=x
# count=0
# while(x!=0):
#     x=x//10
#     count=count+1

# print(count)
# print(y)
# print("-------------------------------")
#reverse no.
ans=0
while(x!=0):
     r=x%10
     x=x//10
     ans=ans*10+r
print(ans)



