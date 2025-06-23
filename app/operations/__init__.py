## Calculator backend
## Evan Garvey
## IS 601, Module 4


## Fairly simple implementation here as all the work is done elsewhere


class Operations:
    
    @staticmethod
    def add(num1: float, num2: float) -> float:

        ## Adds 2 numbers and returns the result.

        ## Params:
        ## num1: float
        ## num2: float

        ## Returns:
        ## num1 + num2: float

        ## example:
        ## >>> add(1, 2)
        ## 3.0

        return num1 + num2

    @staticmethod
    def subtract(num1: float, num2: float) -> float:

        ## Subtracts 2 numbers and returns the result.

        ## Params:
        ## num1: float
        ## num2: float

        ## Returns:
        ## num1 - num2: float

        ## example:
        ## >>> subtract(1, 2)
        ## -1.0

        return num1 - num2

    @staticmethod
    def multiply(num1: float, num2: float) -> float:

        ## Multiplies 2 numbers and returns the result.

        ## Params:
        ## num1: float
        ## num2: float

        ## Returns:
        ## num1 * num2: float

        ## example:
        ## >>> multiply(1, 2)
        ## 2.0

        return num1 * num2

    @staticmethod
    def divide(num1: float, num2: float) -> float:

        ## Divides 2 numbers and returns the result.

        ## Params:
        ## num1: float
        ## num2: float

        ## Returns:
        ## num1 / num2: float

        ## example:
        ## >>> divide(1, 2)
        ## 0.5

        ## divide by zero is handled in the calculator.py

        return num1 / num2

    ## TODO: possibly more operations? ie factorial, exponent, etc