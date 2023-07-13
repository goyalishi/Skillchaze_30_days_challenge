# Day-17
# conversion to lowercase
s=input()
re=''
for i in range(len(s)):
    if s[i] >='A' and s[i]<='Z':
        re+=chr(ord(s[i])-65+97)
    else:
        re+=s[i]
print(re)