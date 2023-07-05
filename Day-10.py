# Day-10
# Maximum Subarray sum (Using Kadane's algorithm)
def max_sum(arr):
    max_sum_sofar=0
    max_sum_now=arr[0]
    for i in range(1,len(arr)):
        max_sum_now+=arr[i]
        if max_sum_now<0:
            max_sum_now=0
        max_sum_sofar=max(max_sum_now,max_sum_sofar)
    return max_sum_sofar

ls=list(map(int,input().split()))
out=max_sum(ls)
print(out)