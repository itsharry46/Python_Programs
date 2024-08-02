# Write a program to find a fibonacci of a number
# a series of numbers in which each number ( Fibonacci number ) is the sum of the two preceding numbers
# Example: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144

def fibonacci(num: int):
    # Define default values
    n1, n2 = 0, 1
    count = 0

    if num <= 0:
        return "The number must be positive"

    elif num == 1:
        return "The fibonacci series of 1 term: 1"

    else:
        res = f"The fibonacci series of {num} term: "

        # Executing the while until the number is reached
        while count < num:
            res = res + f"{str(n1)}, "
            nth = n1 + n2
            n1 = n2
            n2 = nth
            count += 1

        return res.strip(", ")


try:
    # Input keyword is used to take number from command line (Default type String) int() is used to convert into integer
    input_num = int(input("Please enter the term value: "))

    result = fibonacci(input_num)
    print(result)

except ValueError:
    # If value error is raised during the execution of try block it will be traced here
    print("Only numbers are allowed.")