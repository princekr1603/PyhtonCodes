# li=list(input("enter list"))
# ans=0
# for i in li:
#     ans=ans^i
# print(ans)
l=[2,2,5,5,8,6,6,4,4]
n=len(l)
l.sort()
i=0
while(i<n):
    if(l[i]==l[i+1]):
        i=i+2
    else:
        print(l[i])
        break