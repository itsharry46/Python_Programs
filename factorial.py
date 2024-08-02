# Write a program to find a factorial of a number
# It represents the multiplication of all numbers between 1 and n
# 3! = 3x2x1 = 6

def factorial(num: int):
    # defining default factorial result as 1
    fact = 1

    # If number is in negative factorial cannot be existed
    if num < 0:
        return "Sorry, factorial does not exist for negative numbers"

    # Always the factorial of 0 will be 1
    elif num == 0:
        return "The factorial of 0 is 1"

    # Usually range start from 0 i.e range start from 1 to ( num + 1)
    else:
        for i in range(1, num + 1):
            fact = fact * i

        return f"The factorial of {num} is {fact}"


try:
    # Input keyword is used to take number from command line (Default type String) int() is used to convert into integer
    input_num = int(input("Please Enter the first number: "))

    result = factorial(input_num)
    print(result)

except ValueError:
    # If value error is raised during the execution of try block it will be traced here
    print("Only numbers are allowed.")