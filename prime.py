# Write a program to find if the given number is prime or not
# A prime number is a number that can only be divided by itself and 1 without remainders
# For example, 5 is prime because the only ways of writing it as a product, 1 × 5 or 5 × 1, involve 5 itself

def prime(number: int):
    # Defined a flag to identify it is prime number or not
    prime_flag = False

    # If number less than or equal to 1 then it would be prime number
    if number > 1:

        # Running the for loop for the numbers greater than or equal to 2 till number -1
        for i in range(2, number):

            # If any more division is found expect 1 and the actual number then it is marked as non-prime number
            if (number % i) == 0:
                prime_flag = True
                break

    return f"{number} is not a Prime Number" if prime_flag else f"{number} is a Prime Number"


try:
    # Input keyword is used to take number from command line (Default type String) int() is used to convert into integer
    input_num = int(input("Please enter a number: "))
    result = prime(input_num)
    print(result)

except ValueError:
    # If value error is raised during the execution of try block it will be traced here
    print("Only numbers are allowed.")