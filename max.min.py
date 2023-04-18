n=int(input("enter no. of value"))
l=[]
for i in range(n):
    l.append(int(input("enter no")))
max=l[0]
min=l[0]
for i in l:
    if i>max:
        max=i
    if i<min:
        min=i
print("maximum:",max)
print("minimum:",min)
