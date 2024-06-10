from calculator.calculations import Calculations  
from calculator.operations import add, subtract, multiply, divide  
from calculator.calculation import Calculation  
from decimal import Decimal  
from typing import Callable  

# Definition of the Calculator class
class Calculator:
    @staticmethod
    def _solve(a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]) -> Decimal:
        """Create and perform a calculation, then return the result."""
        calculation = Calculation.create(a, b, operation)
        Calculations.add_calculation(calculation)
        return calculation.perform()

    # Perform all operations by delegating to the _solve method with the add operation
    @staticmethod
    def add(a: Decimal, b: Decimal) -> Decimal:
        return Calculator._solve(a, b, add)

    @staticmethod
    def subtract(a: Decimal, b: Decimal) -> Decimal:
        return Calculator._solve(a, b, subtract)

    @staticmethod
    def multiply(a: Decimal, b: Decimal) -> Decimal:
        return Calculator._solve(a, b, multiply)

    @staticmethod
    def divide(a: Decimal, b: Decimal) -> Decimal:
        return Calculator._solve(a, b, divide)
