# Write a program to find Greatest Common Divisor of two numbers
# Which are not all zero, is the largest positive integer that divides each of the integers
# For example, the GCD of 8 and 12 is 4, that is, gcd = 4

def gcd(num1: int, num2: int):

    if num1 == 0:
        return num2

    elif num2 == 0:
        return num1

    elif num1 == num2:
        return num1

    elif num1 > num2:
        return gcd(num1-num2, num2)

    else:
        return gcd(num1, num2-num1)


try:
    # Input keyword is used to take number from command line (Default type String) int() is used to convert into integer
    number_one = int(input("Please enter the first value: "))
    number_two = int(input("Please enter the second value: "))

    result = gcd(number_one, number_two)
    print(f"GCD of number {number_one} and {number_two} is {result}")

except ValueError:
    # If value error is raised during the execution of try block it will be traced here
    print("Only numbers are allowed.")
