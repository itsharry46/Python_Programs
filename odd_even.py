# Write a program to validate given number is odd or even

def validate_even_odd(number):
    try:
        # Ternary operation if the number is even return True else False
        return True if (number % 2) == 0 else False

    except Exception as ex:
        print(ex)


# Execution start
# Used try and catch block to handle error exception while taking the input
# If input type is not of integer then it will go into except block
try:
    # Input keyword is used to take number from command line (Default type String) int() is used to convert into integer
    input_num = int(input("Please Enter a number: "))

    # Calling the function which is defined above and passing the input received from the commandline
    result = validate_even_odd(input_num)
    if result:
        print(f"The number {input_num} is even.")
    else:
        print(f"The number {input_num} is odd.")


except ValueError:
    # If value error is raised during the execution of try block it will be traced here
    print("Only numbers are allowed.")
