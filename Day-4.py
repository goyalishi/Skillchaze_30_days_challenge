# Day-4
ls= eval(input())
set_=set(ls)
for i in set_:
    if ls.count(i)==1:
        print(i)
        break