# Write a program to check if the given number is Armstrong or not
# Armstrong number is a number that is equal to the sum of cubes of its digits
# For example 0, 1, 153, 370, 371 and 407 are the Armstrong numbers
# 153 = (1*1*1)+(5*5*5)+(3*3*3)
# where:
# (1*1*1)=1
# (5*5*5)=125
# (3*3*3)=27
# So: 1+125+27=153

def armstrong(num: int):
    # Defining a temporary variable
    temp = 0

    # In addition, of each cube of integer
    for i in str(num):
        # Adding the result of each cube
        temp += int(i) ** 3

    return f"{num} is a armstrong number" if temp == num else f"{num} is not a armstrong number"


try:
    # Input keyword is used to take number from command line (Default type String) int() is used to convert into integer
    input_num = int(input("Please enter a number: "))
    result = armstrong(input_num)
    print(result)

except ValueError:
    # If value error is raised during the execution of try block it will be traced here
    print("Only numbers are allowed.")