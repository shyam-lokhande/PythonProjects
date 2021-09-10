def FindFact(num):
    if(num==0 or num==1):
        return 1
    return  num* FindFact(num-1)
    

a = int(input("Enter the number to get its factorial :"))
print(f"The factoral of the number {a} is {FindFact(a)}")
