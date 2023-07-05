# Day-11
# Longest subarray of consecutive elements
# Using Kadane's algorithm
ls=eval(input())
long_so_far=1
long_now=1
for i in range(1,len(ls)):
    if ls[i]==ls[i-1]+1:
        long_now+=1
    else:
        long_now=1
    long_so_far=max(long_now,long_so_far)
print(long_so_far)