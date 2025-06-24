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
        exit: Exit the calculator

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
    print("Type 'help' for more information, or 'exit' to exit.")

    ## Loop for user continuous user input and execution

        ## Inputs:

    ## <operation> <num1> <num2>: Valid user input
    ## <invalid operation> <num1> <num2>: Invalid user input
    ## <operation> [List of numbers where length != 2]: Invalid user input

    ## help: Display help message
    ## history: Display command history
    ## exit: Exit the calculator

    ## <KeyboardInterrupt>: Exit the calculator
    ## <EOF Error>: Exit the calculator

        ## Outputs:

    ## result: <Calculation>
    ## Valid calculation

    ## Invalid parameters. Parameters 2 and 3 must be valid floats. Please try again.
    ## Type 'help' for more information.
    ## Invalid params

    ## Invalid calculation type: invalid_operation. Available types: add, subtract, multiply, divide
    ## Type 'help' for more information.
    ## Invalid operation

    ## REPL Calculator help 
    ## [...]
    ## Help operation

    ## Calculation History:
    ## [...]
    ## History operation

    ## Goodbye!
    ## Exit operation (code 0)

    while True:

        try:

            ## Handle an empty user input

            user_input: str = input(">> ").strip()

            if not user_input:

                continue #pragma: no cover

            ## Handle special commands (help, history, exit)

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

                ## Handle user input given a non-special non-empty command

                operation, str1, str2 = user_input.split()
                num1 = float(str1)
                num2 = float(str2)

            except ValueError:

                ## Check for invalid parameters

                print("Invalid parameters. Parameters 2 and 3 must be valid floats. Please try again.")
                print("Type 'help' for more information.")
                continue

            try:

                ## User input is then parsed and handled by CalculationFactory

                calculation = CalculationFactory.create_calculations(operation, num1, num2)

            except ValueError as ve:

                ## Catches invalid operations sent from the CalculationFactory

                print(ve)
                print("Type 'help' for more information.")
                continue

            try:

                ## Execute the calculation, once all parameters are confirmed as valid

                print("Executing calculation...")
                result = calculation.execute()
                print(result)

            ## This is redundant as it gets caught by the except Exception

            #except ZeroDivisionError:

                #print("Cannot divide by zero. Please try again.")
                #print("Type 'help' for more information.")
                #continue

            except Exception as e:

                ## Catch any other errors that occur strictly during the calculation

                print(e)
                print(f"An error occurred: {e} Please try again.")
                print("Type 'help' for more information.")
                continue

            ## Display the calculation and add it to the history

            result_str: str = f"{calculation}"
            print(f"result: {result_str}\n")
            history.append(calculation)\
            
        except KeyboardInterrupt:

            ## Handle keyboard interrupts

            print("\nKeyboard Interrupt detected. Goodbye!")
            sys.exit(0)

        except EOFError:

            ## Handle EOF errors

            print("\nEOF detected. Goodbye!")
            sys.exit(0)


if __name__ == "__main__":

    calculator() #pragma: no cover