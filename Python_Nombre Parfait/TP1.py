def parfait(n):
    x = 1
    for i in range (n//2, 1, -1):
        if (n % i == 0):
            x = x + i
        if x == n:
            return 1
    return 0

num = int(input("enter the number"))
result = 0
for i in range(1,num):
    if (num%i)==0:
        result=result+i
if result==num:
    print(num,"is perfect number")
else:
    print(num,"is not perfect number")


def fct_tri(c, l):
    for i in range(len(l)):
        if l[i]==c:
            return True
    return False
