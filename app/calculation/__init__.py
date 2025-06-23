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
    
## Factory class for calculations

class CalculationFactory:

    ## initialize a dictionary for mapping calculation types

    _calculations = {}

    @classmethod
    def register_calculation(cls, type: str):

        ## Registers a new calculation type.

        ## Params:
        ## type: str

        ## Returns:
        ## decorator: function call (which in turn gives us a registered subclass)

        def decorator(subclass):

            ## Decorator function to register a new calculation type.

            ## Params:
            ## subclass: A subclass of Calculation

            ## Returns:
            ## Subclass: The registered subclass

            type_lower = type.lower()
            if type_lower in cls._calculations:

                raise ValueError (f"Calculation type {type_lower} is already registered.")
            
            cls._calculations[type_lower] = subclass
            return subclass

        return decorator
    
    @classmethod
    def create_calculations(cls, type: str, num1: float, num2: float) -> Calculation:

        ## Creates a new calculation instance.

        ## Params:
        ## type: str
        ## num1: float
        ## num2: float

        ## Returns:
        ## Calculation: A new instance of the specified calculation type

        type_lower = type.lower()
        calculation_class = cls._calculations.get(type_lower)

        if not calculation_class:

            available_types = ', '.join(cls._calculations.keys())
            raise ValueError(f"Invalid calculation type: {type}. Available types: {available_types}")
        
        return calculation_class(num1, num2)