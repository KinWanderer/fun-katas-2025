# Function to calculate the divisors of a given number
def calculate_divisors(number):
    divisors = [0]
    for i in range(1, number):
        if (number % i)==0:
            divisors.append(i)
    return sum(divisors)