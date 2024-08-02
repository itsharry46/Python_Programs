# Write a program to print the following pattern
#     *
#    * *
#   * * *
#  * * * *
# * * * * *

def triangle(num: int):
    k = num - 1

    for i in range(num):
        for j in range(k):
            print(end=" ")

        k = k - 1
        for j in range(i + 1):
            print("* ", end="")
        print("\r")


try:
    # Input keyword is used to take number from command line (Default type String) int() is used to convert into integer
    input_num = int(input("Please enter the length of star pattern: "))
    triangle(input_num)

except ValueError:
    # If value error is raised during the execution of try block it will be traced here
    print("Only numbers are allowed.")