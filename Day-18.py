# Day-18
# Power of string(Using Kadane's algorithm)
s=input()
max_pow=pow=1
for i in range(1,len(s)):
    if s[i]==s[i-1]:
        pow+=1
    else:
        pow=1
    max_pow=max(pow,max_pow)
print(max_pow)