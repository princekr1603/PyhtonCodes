a=str(input("enter string"))
b=a.lower()
cnt=0
for i in range(0,len(a)):
    if(a[i]==b[i]):
        cnt=cnt+1
print(cnt)

print("------------------------------------")
#A-65,Z=90 ||a=97,z=122||32-space||0-48,9-57JJDCGDJCHBG
x=input()
cnt=0
CAP=0
for i in x:
    if (i>="a" and i<="z"):
        cnt=cnt+1
    else:
        CAP+=1
print(cnt,CAP)