## Calculator Interface
## Evan Garvey
## IS 601, Module 4

from app.operations import add, subtract, multiply, divide


## This calculator is heavily based on the previous calculator that we made in module 3.
## I am performing changes where needed (primarily in the error handling) in order to ensure best practices

def is_float(num):
    if num.count('.') > 1:
        return False
    if num[0] == '-':
        num = num[1:]
    return num.replace('.', '', 1).isdigit()


def calculator():

    print("Welcome to the Calculator Interface! Type 'quit' at any time to exit.")
    print("_____________________________________________________________________")

    while True:

        user_input = input("Enter a desired operation (add, subtract, multiply, divide), and then two numbers separated by a space. Type 'quit' to exit. \n")

        ## Check if an exit is desired

        if user_input.lower() == "quit":
            print("Goodbye!")
            break

        ## Check if operation is in valid form
        ## This, as well as is_float, follow LBYL

        if len(user_input.split()) != 3:
            print("Invalid parameters. 3 Parameters are required (operation, num1, num2). Please try again.")
            continue

        operation, num1, num2 = user_input.split()

        if not (is_float(num1) and is_float(num2)):
            print("Invalid parameters. Parameters 2 and 3 must be valid floats. Please try again.")
            continue

        num1, num2 = float(num1), float(num2)

#        Old approach, was EAFP but has been replaced by LBYL
#
#        try:
#
#            operation, num1, num2 = user_input.split()
#            num1, num2 = float(num1), float(num2)
#
#        except ValueError:
#
#            print("Invalid input. Please try again.")
#            continue

        ## Once operation has been validated, parse and compute

        if operation == "add":
            result = add(num1, num2)

        elif operation == "subtract":
            result = subtract(num1, num2)

        elif operation == "multiply":
            result = multiply(num1, num2)

        ## Division is a bit tricky as we have to watch out for division by 0

        elif operation == "divide":

            ## Example of EAFP approach

            try:
                result = divide(num1, num2)

            except ZeroDivisionError:
                print("Cannot divide by zero. Please try again.")
                continue

        else:
            print("Invalid operation. Please try again.")
            continue

        print(f"Result: {result}")