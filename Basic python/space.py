n=input()
a=input("enter")
s=""

for i in n:
    c=0
    for j in range(len(n)):
        if(i==n[j]):
            c+=1
        if(i not in s and i==a):
            print(i,":",c)
            s+=i