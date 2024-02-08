from fuel import convert, gauge
import pytest


def main():
     # Calling the test functions
    test_zero_division()
    test_value_error()
    test_correct_output()

# Test function to check if the 'convert' function raises a ZeroDivisionError for an invalid fraction
def test_zero_division():
    # Using 'pytest.raises' to check if a ZeroDivisionError is raised when calling 'convert' with '1/0'
    with pytest.raises(ZeroDivisionError):
        convert('1/0')


def test_value_error():
    with pytest.raises(ValueError):
        convert("cat/dog")

# Test function to check if the 'convert' and 'gauge' functions produce correct output for valid fractions
def test_correct_output():
    # Asserting that 'convert' with '1/4' should return 25 and 'gauge' with 25 should return '25%'
    assert convert('1/4') == 25 and gauge(25) == '25%'
    assert convert('1/100') == 1 and gauge(1) == 'E'
    assert convert('99/100') == 99 and gauge(99) == 'F'

if __name__ == "__main__":
    main()
