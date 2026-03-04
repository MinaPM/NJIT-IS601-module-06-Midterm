##############
# Linearizer #
##############
from app.calculator import Calculator
from app.operations import OperationFactory
import re


class Linearizer:
    """
        Adapter that converts written mathematical expressions into symbolic expressions
        evaluable by the calculator.
    """

    mapping = {
        '+': 'add',
        '-': 'subtract',
        '*': 'multiply',
        '/': 'divide',
        '^': 'power',
        '#': 'root',
        '&': 'modulus',
        '\\': 'int_divide',
        '%': 'percent',
        '|': 'abs_diff'
    }

    def __init__(self, expression: str):
        self.expression = expression
        self.a = 0
        self.b = 0
        self.operator = ''
        self.operation_name = ''

    def set_expression(self, expression: str) -> None:
        """
            Update the expression to be linearized.

            Args:
                expression (str): The new mathematical expression to linearize.
        """
        self.expression = expression

    def get_operation_name(self, symbol: str) -> str:
        """
            Maps mathematical symbols to their corresponding operation names.

            Args:
                symbol (str): The mathematical symbol to map.

            Returns:
                str: The name of the corresponding operation.

            Raises:
                ValueError: If the symbol is not recognized as a valid operation.
        """

        if symbol not in self.__class__.mapping:
            raise ValueError(f"Unrecognized symbol: {symbol}")

        return self.__class__.mapping[symbol]

    def parse(self):
        """
            Parses the input expression and extracts the operands and operator.
            The expression is expected to be in the format: <number><operator><number>.
            Raises:
                ValueError: If the expression format is invalid or if operands are not numeric.
        """
        pattern = r'^(\d+(?:\.\d+)?)\s*([+\-*/^#&\\%|])\s*(\d+(?:\.\d+)?)$'

        match = re.match(pattern, self.expression)
        if not match:
            raise ValueError(
                "Invalid expression format. Expected format: <number><operator><number>")

        experssionParts = match.groups()

        if len(experssionParts) != 3:
            raise ValueError(
                "Invalid expression format. Expected format: <number><operator><number>")

        self.a, self.operator, self.b = [
            part.strip() for part in experssionParts]

        if not self.a or not self.operator or not self.b:
            raise ValueError(
                "Invalid expression format. Missing operand or operator.")

        if not self.a.replace('.', '', 1).isdigit() or not self.b.replace('.', '', 1).isdigit():
            raise ValueError(
                "Invalid expression format. Operands must be numeric.")

        self.operation_name = self.get_operation_name(self.operator)
