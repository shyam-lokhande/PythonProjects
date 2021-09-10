a =int(input("Enter the starting number of fibonacci series :"))
b =int(input("Enter the second number of fibonacci series :"))
n = int(input("How many terms do you want in fibonacci series :"))

print(a,b,end=" ")
while n-2:
    c=a+b
    a=b
    b=c
    print(c,end=" ")
    n-=1
