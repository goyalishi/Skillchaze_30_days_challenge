# Day-9
# Subarray with sum 0
def subarray(ls,sum_):
    for i in range(len(ls)):
        s=0
        for j in range(i,len(ls)):
            s+=ls[j]
            if s==sum_:
                return True
    return False

ls=list(map(int,input().split()))
sum_=0
print(subarray(ls,sum_))

