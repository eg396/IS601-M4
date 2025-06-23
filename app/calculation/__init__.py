## Calculator backend helper
## Evan Garvey
## IS 601, Module 4

## Import abstract class and methods
from abc import ABC, abstractmethod

## Import our operations module
from app.operations import Operations

## Abstract calculation class

class Calculation(ABC):

    @abstractmethod
    def __init__(self, num1: float, num2: float) -> None:

        ## Initializes the two parameters as floats.

        ## Params:
        ## num1: float
        ## num2: float

        ## Returns:
        ## N/A as this is an abstract method

        self.num1: float = num1
        self.num2: float = num2

    @abstractmethod
    def execute(self) -> float:

        ## Executes the calculation and returns the result.

        ## Returns: 
        ## N/A as this is an abstract method

        pass    ## pragma: no cover

    def __str___(self) -> str:

        ## Returns a string representation of the calculation instance

        ## Returns:
        ## str: A string representation of the calculation

        result = self.execute()
        operation = self.__class__.__name__.replace('Calculation', '')
        return f"{self.__class__.__name__}: {self.num1} {operation} {self.num2} = {result}"
    
    def __repr__(self) -> str:

        ## Returns a string representation of the calculation instance

        ## Returns:
        ## str: A string representation of the calculation

        return f"{self.__class__.__name__}(num1 = {self.num1}, num2 = {self.num2})"