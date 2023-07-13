# Day-19
# Power of Two
def power(n):
    if n==1:
        return True
    elif n%2!=0 or n==0:
        return False
    else:
        if n>=4 and n%4==0:
            q=n//4
        else:
             q=n//2
        if 2**q==n:
            return True
        else:
            return power(q)
n=int(input())
print(power(n))

# another approach
n=int(input())
i=1
flag=False
while i<=n:
    if i==n:
        print(True)
        break
    else:
        i*=2
        if i==n:
            flag=True
            break
if flag:
    print(True)
else:
    if i!=1:
        print(False)