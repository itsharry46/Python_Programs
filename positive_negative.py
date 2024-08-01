# Write a program to find the given number is positive or negative

# Defining the function with parameter input of number dataType
def positive_negative(num: int):
    # If the number is 0 marking it as neutral number
    if num == 0:
        return f"The number {num} is neutral"

    # If the above condition does not satisfy then below condition will execute. Validating the number is greater than 0 or not
    elif num > 0:
        return f"The number {num} is positive"

    # If all the above condition is not satisfactory then else block get executed
    else:
        return f"The number {num} is negative"


try:
    # Input keyword is used to take number from command line (Default type String) int() is used to convert into integer
    input_num = int(input("Please enter a number: "))

    # Calling the function which is defined above and passing input_num as parameter, which is received from the commandline
    result = positive_negative(input_num)
    print(result)

except ValueError:
    # If value error is raised during the execution of try block it will be traced here
    print("Only numbers are allowed.")
