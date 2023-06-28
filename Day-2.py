# DAY-2
# FizzBuzz
def fizzbuzz(n):
    ls=[]
    for i in range(1,n+1):
        if i%3==0 and i%5==0:
            ls.append("FizzBuzz")
        elif i%5==0:
            ls.append("Buzz")
        elif i%3==0:
            ls.append("Fizz")
        else:
            ls.append(i)
    return ls
num=int(input())
out=fizzbuzz(num)
print(out)