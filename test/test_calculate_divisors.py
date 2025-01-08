from src.calculate_divisors import calculate_divisors

# 1. return 0 if input number is 1
def test_calculate_divisor_of_1_to_return_zero():
    # Assemble
    input_number = 1

    # Act
    output = calculate_divisors(input_number)
    expected_output = []

    # Assert
    assert output == expected_output

# 2. return 3 with input number 5
def test_calculate_divisor_of_6_to_return_3():
    # Assemble
    input_number = 5

    # Act
    output = calculate_divisors(input_number)
    expected_output = [3]

    # Assert
    assert output == expected_output