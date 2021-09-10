def IsPalindrome(Input):
    reverse = Input[::-1]
    if(reverse==Input):
        return f"Given input is Palindrome. Your input {Input} is equal to its reverse {reverse}"
    return "Given input is not Palindrome.  Your input {Input} is not equal to its reverse {reverse}"

In = input("Enter your input :")
print(IsPalindrome(In))
