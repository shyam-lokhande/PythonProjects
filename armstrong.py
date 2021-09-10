def IsArmstrong(n):
    sumOfCubeOfDigits=0
    temp=n
    while temp>0:
        remain=temp%10
        sumOfCubeOfDigits+=remain**3
        temp//=10
    if (sumOfCubeOfDigits==n):
        return f"Entered number {n} is an armstrong number."
    return f"Entered number {n} is not an armstrong number."
        
Num = int(input("Enter the number to check whether the number is armstrong or not :"))
print(IsArmstrong(Num))