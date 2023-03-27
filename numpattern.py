x=int(input())
num=2*x-1

l=[[0 for x in range (num)] for y in range (num) ]

xt=(num+1)//2
n=1
low=0
high=num-1

k=1

for i in range(xt):
    for j in range(low,high+1):
        l[low][j]=k
        
    for j in range (low+1,high+1):
        l[j][high]=k
        
    for j in range(high-1,low-1,-1):
        l[high][j]=k
        
    for j in range(high-1,low-1,-1):
        l[j][low]=k 

        
    low=low+1
    high=high-1
    k+=1

for i in range(num):
    for j in range(num):
        print(l[i][j],end="\t")
    print()
