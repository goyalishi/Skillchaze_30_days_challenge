# Phrase is Palindrome?
def isPalindrome(s):
    s1=s.replace(' ','').lower()
    st=''
    for i in range(len(s1)):
        if s1[i].isalnum():
            st+=s1[i]
    if st==st[::-1]:
        return True
    else:
        return False
    
s=input()
print(isPalindrome(s))
    