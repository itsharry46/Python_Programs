# Write a program to find a maximum of two numbers

def max_number(num1: int, num2: int):
    if num1 == num2:
        return "Both the numbers are same"

    return f"{num1} is the maximum number" if num1 > num2 else f"{num2} is the maximum number"


try:
    # Input keyword is used to take number from command line (Default type String) int() is used to convert into integer
    number_one = int(input("Please Enter the first number: "))
    number_two = int(input("Please Enter the second number: "))

    result = max_number(number_one, number_two)
    print(result)

except ValueError:
    # If value error is raised during the execution of try block it will be traced here
    print("Only numbers are allowed.")