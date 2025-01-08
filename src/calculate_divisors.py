# a func with SUMS all the MULTIPLES of 3 and 5 
# belew an input number

def sum_divisors(number):
    if not isinstance(number, int) or number <= 0:
        raise ValueError("Input number must be a positive integer")
    
    divisors = []
    for i in range(1, number):
        if i % 3 == 0 or i % 5 == 0:
            divisors.append(i)

    return sum(divisors)