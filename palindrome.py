# Write a program to check if the given number is palindrome or not
# A palindromic number is a number that remains the same when its digits are reversed
# Example 11, 121, 75257

def palindrome(num: int):
    # Converted that number into a string, so I can perform string reverse operation and finally converted back the variable into integer
    # First way using extended slice
    # Second way using reversed function

    # temp = int(str(num)[::-1])
    temp = int("".join(reversed(str(num))))

    return f"{num} is Palindrome Number" if num == temp else f"{num} is not Palindrome Number"


try:
    # Input keyword is used to take number from command line (Default type String) int() is used to convert into integer
    input_num = int(input("Please enter a number: "))
    result = palindrome(input_num)
    print(result)

except ValueError:
    # If value error is raised during the execution of try block it will be traced here
    print("Only numbers are allowed.")