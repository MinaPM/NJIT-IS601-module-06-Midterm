import pytest
from app.linearizer import Linearizer


class TestLinearizer:
    """Test suite for the Linearizer class."""

    def test_init(self):
        """Test initialization of Linearizer."""
        linearizer = Linearizer("5+3")
        assert linearizer.expression == "5+3"
        assert linearizer.a == 0
        assert linearizer.b == 0
        assert linearizer.operator == ''
        assert linearizer.operation_name == ''

    def test_set_expression(self):
        """Test set_expression method."""
        linearizer = Linearizer("5+3")
        linearizer.set_expression("10-2")
        assert linearizer.expression == "10-2"

    def test_get_operation_name_valid_symbols(self):
        """Test get_operation_name with valid symbols."""
        linearizer = Linearizer("")
        assert linearizer.get_operation_name('+') == 'add'
        assert linearizer.get_operation_name('-') == 'subtract'
        assert linearizer.get_operation_name('*') == 'multiply'
        assert linearizer.get_operation_name('/') == 'divide'
        assert linearizer.get_operation_name('^') == 'power'
        assert linearizer.get_operation_name('#') == 'root'
        assert linearizer.get_operation_name('&') == 'modulus'
        assert linearizer.get_operation_name('\\') == 'int_divide'
        assert linearizer.get_operation_name('%') == 'percent'
        assert linearizer.get_operation_name('|') == 'abs_diff'

    def test_get_operation_name_invalid_symbol(self):
        """Test get_operation_name with invalid symbol."""
        linearizer = Linearizer("")
        with pytest.raises(ValueError, match="Unrecognized symbol"):
            linearizer.get_operation_name('$')

    def test_parse_valid_addition(self):
        """Test parse with valid addition expression."""
        linearizer = Linearizer("5+3")
        linearizer.parse()
        assert linearizer.a == '5'
        assert linearizer.b == '3'
        assert linearizer.operator == '+'
        assert linearizer.operation_name == 'add'

    def test_parse_valid_subtraction(self):
        """Test parse with valid subtraction expression."""
        linearizer = Linearizer("10-2")
        linearizer.parse()
        assert linearizer.a == '10'
        assert linearizer.b == '2'
        assert linearizer.operator == '-'
        assert linearizer.operation_name == 'subtract'

    def test_parse_valid_multiplication(self):
        """Test parse with valid multiplication expression."""
        linearizer = Linearizer("6*7")
        linearizer.parse()
        assert linearizer.a == '6'
        assert linearizer.b == '7'
        assert linearizer.operator == '*'
        assert linearizer.operation_name == 'multiply'

    def test_parse_valid_division(self):
        """Test parse with valid division expression."""
        linearizer = Linearizer("20/4")
        linearizer.parse()
        assert linearizer.a == '20'
        assert linearizer.b == '4'
        assert linearizer.operator == '/'
        assert linearizer.operation_name == 'divide'

    def test_parse_with_decimals(self):
        """Test parse with decimal numbers."""
        linearizer = Linearizer("5.5+3.2")
        linearizer.parse()
        assert linearizer.a == '5.5'
        assert linearizer.b == '3.2'
        assert linearizer.operator == '+'

    def test_parse_with_spaces(self):
        """Test parse with spaces around operator."""
        linearizer = Linearizer("5 + 3")
        linearizer.parse()
        assert linearizer.a == '5'
        assert linearizer.b == '3'
        assert linearizer.operator == '+'

    def test_parse_invalid_format_too_many_parts(self):
        """Test parse with invalid format (too many parts)."""
        linearizer = Linearizer("5+3+2")
        with pytest.raises(ValueError, match="Invalid expression format. Expected format: <number><operator><number>"):
            linearizer.parse()

    def test_parse_invalid_format_missing_operand(self):
        """Test parse with missing operand."""
        linearizer = Linearizer("5+")
        with pytest.raises(ValueError, match="Invalid expression format. Expected format: <number><operator><number>"):
            linearizer.parse()

    def test_parse_all_operators(self):
        """Test parse with all supported operators."""

        for op, op_name in Linearizer.mapping.items():
            linearizer = Linearizer(f"2{op}3")
            linearizer.parse()
            assert linearizer.operation_name == op_name
