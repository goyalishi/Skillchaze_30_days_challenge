# Day-7
# Binary to decimal conversion
def bintodec(s):
    st=s[::-1]
    num=0
    for i in range(len(st)):
        num+=int(st[i])*(2**i)
    return num

s=input("Enter the binary string")
dec=bintodec(s)
print(dec)