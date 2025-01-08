from src.calculate_divisors import sum_divisors

class TestCalculateDivisors:
# 1. return 0 if input number is 1
    def test_calculate_divisor_of_1_to_return_zero(self):
        # Assemble
        input_number = 1

        # Act
        output = sum_divisors(input_number)
        expected_output = 0

        # Assert
        assert output == expected_output

    # 2. return 3 with input number 5
    def test_calculate_divisor_of_6_to_return_3(self):
        # Assemble
        input_number = 5

        # Act
        output = sum_divisors(input_number)
        expected_output = 3

        # Assert
        assert output == expected_output

    # 3. return 8 with input number 6
    def test_calculate_divisor_of_8_to_return_6(self):
        # Assemble
        input_number = 6

        # Act
        output = sum_divisors(input_number)
        expected_output = 8

        # Assert
        assert output == expected_output

    # 4. return 23 with input number 10
    def test_calculate_divisor_of_10_to_return_23(self):
        # Assemble
        input_number = 10

        # Act
        output = sum_divisors(input_number)
        expected_output = 23

        # Assert
        assert output == expected_output

    # 5 return 33 with input number 12

    def test_calculate_divisor_of_12_to_return_33(self):
         # Assemble
        input_number = 12

        # Act
        output = sum_divisors(input_number)
        expected_output = 33

        # Assert
        assert output == expected_output

class TestExpectedFails:
    def test_returns_ValueError_if_input_is_negative(self):
        try: 
            sum_divisors(-1)
        except ValueError as e:
            assert str(e) == "Input number must be a positive integer"
    
    def test_returns_ValueError_if_input_is_float(self):
        try:
            sum_divisors(3.7)
        except ValueError as e:
            assert str(e) == "Input number must be a positive integer"
        
    def test_returns_ValueError_if_input_is_string(self):
        try:
            sum_divisors("Three")
        except ValueError as e:
            assert str(e) == "Input number must be a positive integer"