# Write a Python function that prints the numbers from 1 to 100
# But for multiples of three, print "Fizz" instead of the number and for the multiples of five, print "Buzz"
# For numbers which are multiples of both three and five, print "FizzBuzz"

def fizzbuzz():
    number = 1

    while number <= 30:
        if ((number % 3) == 0) and ((number % 5) == 0):
            print("FizzBuzz")

        elif (number % 3) == 0:
            print("Fizz")

        elif (number % 5) == 0:
            print("Buzz")

        else:
            print(number)

        number += 1
    return True


fizzbuzz()