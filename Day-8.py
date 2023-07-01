# Day-8
# Two sum
nums=list(map(int,input().split()))
target=int(input())
l=len(nums)
for i in range(l-1):
    for j in range(i+1,l):
        if nums[i]+nums[j]==target:
            print([i,j])
            break
        else:
            continue
