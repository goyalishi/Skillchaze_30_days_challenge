# Day-20
# Search insert position
def func(nums,target):
    left=0
    right=len(nums)-1
    while(left<=right):
        mid=(left+right)//2
        if nums[mid]==target:
            return mid
        elif nums[mid]<target:
            left=mid+1
        elif nums[mid]>target:
            right=mid-1
        
    if nums[mid]<target:
        return mid+1
    elif nums[mid]>target:
        return mid      

nums = eval(input())
target = int(input())
print(func(nums,target))