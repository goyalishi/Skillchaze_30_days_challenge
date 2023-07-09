# Day-14
# First non repeating character
def Firstnon_repeat_ch(st):
    for i in range(len(st)):
        if st.count(st[i])==1:
            return i
    return -1

st=input()
print(Firstnon_repeat_ch(st))
