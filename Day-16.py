# Day-16
# Valid Parenthesis
def validp(s):
    ls=[]
    if (s.count('(')==s.count(')') and s.count('{')==s.count('}') and s.count('[')==s.count(']')):
        for i in s:
            if i=='(' or i=='{' or i=='[':
                ls.append(i)
            elif i==')':
                if '('in ls and ls[-1]=='(':
                    ls.pop(-1)
                else:
                    return False
            elif i=='}':
                if '{'in ls and ls[-1]=='{':
                    ls.pop(-1)
                else:
                    return False
            elif i==']':
                if '['in ls and ls[-1]=='[':
                    ls.pop(-1)
                else:
                    return False
        if len(ls)==0:
            return True
        else:
            return False
    else:
        return False
    
s=input()
print(validp(s))