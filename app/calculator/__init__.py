## Calculator Interface
## Evan Garvey
## IS 601, Module 4

## Import many things

import sys
import readline
from typing import List
from app.calculation import CalculationFactory, Calculation

def display_help() -> None:

    ## Displays info for the user

    ## Returns:
    ## N/A

    help_text = """
    REPL Calculator help
          
    Usage:
        <operation> <num1> <num2>
        Perform a specified operation on two submitted numbers.
        Supported operations: 
            add: adds two numbers
            subtract: subtracts two numbers
            multiply: multiplies two numbers
            divide: divides two numbers

    Special Commands:
        help: Display this message
        history: Display the command history
        quit: Exit the calculator

    Examples: 
        add 1 2
        subtract 1 2
        multiply 1 2
        divide 1 2
    """

    print(help_text)

def display_history(history: List[Calculation]) -> None:

    ## Displays the command history

    ## Params:
    ## history: List[str]

    ## Returns:
    ## N/A

    if not history:
        print("Error: No calculations in history.")
    else:
        print("Calculation History:")
        for idx, calculation in enumerate(history, start=1):
            print(f"{idx}. {calculation}")


def calculator() -> None:

    ## Main calculator function

    ## Returns:
    ## N/A

    history: List[Calculation] = []

    print("Welcome to the professional REPL Calculator interface!")
    print("Type 'help' for more information, or 'quit' to exit.")

    while True:

        try:

            user_input: str = input(">> ").strip()

            if not user_input:

                continue

            command = user_input.lower()
            if command == "help":

                display_help()
                continue

            elif command == "history":

                display_history(history)
                continue

            elif command == "exit":

                print("Goodbye!")
                sys.exit(0)

            try:

                operation, str1, str2 = user_input.split()
                num1 = float(str1)
                num2 = float(str2)

            except ValueError:

                print("Invalid parameters. Parameters 2 and 3 must be valid floats. Please try again.")
                print("Type 'help' for more information.")
                continue

            try:

                calculation = CalculationFactory.create_calculations(operation, num1, num2)

            except ValueError as ve:

                print(ve)
                print("Invalid operation. Please try again.")
                print("Type 'help' for more information.")
                continue

            try:

                result = calculation.execute()

            except ZeroDivisionError:

                print("Cannot divide by zero. Please try again.")
                print("Type 'help' for more information.")
                continue

            except Exception as e:

                print(e)
                print(f"An error occurred: {e}. Please try again.")
                print("Type 'help' for more information.")
                continue

            result_str: str = f"{calculation}"
            print(f"result: {result_str}\n")
            history.append(calculation)\
            
        except KeyboardInterrupt:

            print("\nKeyboard Interrupt detected. Goodbye!")
            sys.exit(0)

        except EOFError:

            print("\nEOF detected. Goodbye!")
            sys.exit(0)


if __name__ == "__main__":

    calculator()