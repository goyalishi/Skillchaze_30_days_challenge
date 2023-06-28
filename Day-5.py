# Day-5
# Missing number
ls=eval(input())
ref1=set([i for i in range(1,ls[-1]+1)])
ref2=set(ls)
print(*(ref1 - ref2))
