from plates import is_valid

def main():
     # Call the functions
    test_min_and_max_characters()
    test_start_with_two_letters()
    test_numbers_in_middle()
    test_numbers_zero()
    test_punctuation()

# Plates can contain a maximum of 6 characters or a minimum of 2 characters
def test_min_and_max_characters():
    assert is_valid('AA') == True
    assert is_valid('AbCDEF') == True
    assert is_valid('A') == False
    assert is_valid('ABCDFGH') == False

# Plates initiate with 2 letters
def test_start_with_two_letters():
    assert is_valid('AA') == True
    assert is_valid('A2') == False  # This should be False
    assert is_valid('22') == False

# Plates cannot have numbers in the middle
def test_numbers_in_middle():
    assert is_valid('AAA222') == True
    assert is_valid('AAA22A') == False

# Numbers cannot be zero '0'
def test_numbers_zero():
    assert is_valid('CS50') == True
    assert is_valid('CS05') == False
    assert is_valid('CS50P') == False

# No periods, spaces, or punctuations
def test_punctuation():
    assert is_valid('PI3.14') == False
    assert is_valid('PI3!14') == False
    assert is_valid('PI 14') == False

if __name__ == "__main__":
    main()
