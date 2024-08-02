# Write a program to print the following pattern
# *
# * *
# * * *
# * * * *
# * * * * *

def left_triangle(num: int):
    for i in range(1, num + 1):
        print("* " * i)


try:
    # Input keyword is used to take number from command line (Default type String) int() is used to convert into integer
    input_num = int(input("Please enter the length of star pattern: "))
    left_triangle(input_num)

except ValueError:
    # If value error is raised during the execution of try block it will be traced here
    print("Only numbers are allowed.")