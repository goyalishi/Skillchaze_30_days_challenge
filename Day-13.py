# Day-13
# Compressed String
def compress(st):
    comp_st=''
    c=1
    for i in range(len(st)-1):
        if st[i]==st[i+1]:
            c+=1
        elif st[i]!=st[i+1]:
            comp_st+=st[i]+str(c)
            c=1
    comp_st+=st[-1]+str(c)
    if len(comp_st)<len(st):
        return comp_st
    else:
        return st
        

s=input("Enter the string")
print(compress(s))
