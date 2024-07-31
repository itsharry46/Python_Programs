# Write a program to validate given number is odd or even.

def validate_even_odd(number):
    try:
        if (number % 2) == 0:
            print(f"The number {number} is even.")

        else:
            print(f"The number {number} is odd.")

    except Exception as ex:
        print(ex)


try:
    input_num = int(input("Please Enter a number: "))
    validate_even_odd(input_num)

except ValueError:
    print("Only numbers are allowed.")
