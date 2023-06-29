# Day-6
#  Check Anagram
l=int(input("Enter the length of string"))
str1=sorted(input("Enter first string"))
str2=sorted(input("Enter second string"))
if str1==str2:
    print("Yes, strings are anangrams")
else:
    print("no,strings are not anagrams")
