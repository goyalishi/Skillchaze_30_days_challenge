# Day-15
# longest common prefix string 
def pre_str(strs):
    out=''
    strs.sort(key=len)
    for i in range(len(strs[0])):
        ls=[strs[j][i] for j in range(len(strs))]
        if [strs[0][i]]*len(strs) ==ls:
            out+=strs[0][i]
        else:
            break
    return out

strs=eval(input())
pre_st=pre_str(strs)
print(pre_st)