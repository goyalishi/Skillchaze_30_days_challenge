# Day-21
n=int(input())
ls=sum([i for i in range(1,n+1) if i%3==0 or i%5==0 or i%7==0])
print(ls)