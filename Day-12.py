# Day-12
# String Rotation(rightwards)
def rotate(l1):
    last=l1[-1]
    for i in range(len(l1)-2,-1,-1):
        l1[i+1]=l1[i]
    l1[0]=last
    return l1

st1=list(input())
st2=list(input())
flag=0
for i in range(len(st1)-1):
    re=rotate(st1)
    if re==st2:
        print("True")
        flag=1
        break
if flag==0:
    print("False")    

             