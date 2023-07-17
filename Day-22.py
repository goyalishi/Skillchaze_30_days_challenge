# Day-22
# is Isomorphic
def isIsomorphic(s,t):
    dct={}
    for i in range(len(s)):
        a1,a2=s[i],t[i]
        if a1 in dct:
            if dct[a1]!=a2:
                return False
        else:
            if a2 in dct.values():
                return False
            else:
                dct[a1]=a2

    return True

s=input()
t=input()
print(isIsomorphic(s,t))