## Calculator Interface
## Evan Garvey
## IS 601, Module 3

from app.operations import add, subtract, multiply, divide


## This calculator is heavily based on the previous calculator that we made in module 2.
## However, this time, I have started completely from scratch and will only be referencing module 2 for the operations.
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

        try:

            operation, num1, num2 = user_input.split()
            num1, num2 = float(num1), float(num2)

        except ValueError:

            print("Invalid input. Please try again.")
            continue

        ## Once operation has been validated, parse and compute

        if operation == "add":
            result = add(num1, num2)

        elif operation == "subtract":
            result = subtract(num1, num2)

        elif operation == "multiply":
            result = multiply(num1, num2)

        ## Division is a bit tricky as we have to watch out for division by 0

        elif operation == "divide":

            try:
                result = divide(num1, num2)

            except ZeroDivisionError:
                print("Cannot divide by zero. Please try again.")
                continue

        else:
            print("Invalid operation. Please try again.")
            continue

        print(f"Result: {result}")