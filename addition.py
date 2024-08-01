# Write a program to find the sum of two numbers

# Defining the function with parameter input of number dataType
def addition(num_1: int, num_2: int):
    # Addition of both the numbers and returning it back
    return num_1 + num_2


try:
    # Input keyword is used to take number from command line (Default type String) int() is used to convert into integer
    first_no = int(input("Enter the first number: "))
    second_no = int(input("Enter the second number: "))

    # Passing the above two input as parameter in the below function
    result = addition(first_no, second_no)
    print(f"Addition of {first_no} and {second_no} = {result}")

except ValueError:
    # If value error is raised during the execution of try block it will be traced here
    print("Only numbers are allowed.")
