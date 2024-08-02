# Write a program to print the following pattern
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15

def num_pattern(num: int):
    count = 1
    for i in range(1, num + 1):
        for j in range(1, i + 1):
            print(count, end=" ")
            count += 1

        print("\r")


try:
    # Input keyword is used to take number from command line (Default type String) int() is used to convert into integer
    input_num = int(input("Please enter the length of star pattern: "))
    num_pattern(input_num)

except ValueError:
    # If value error is raised during the execution of try block it will be traced here
    print("Only numbers are allowed.")