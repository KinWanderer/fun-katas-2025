"""The challenge is to implement a function 
which cashes up a till at the end of the day. 
The function should always return a string.

The till contents should be a dictionary in this format:

"""

till = {
  "1p": 1,
  "2p": 1,
  "5p": 1,
  "10p": 1,
  "20p": 1,
  "50p": 1,
  "£1": 1,
  "£2": 1,
  "£5": 1,
  "£10": 1,
  "£20": 1,
  "£50": 1
}

# a func SUMS till to return a total STRING
# inilise SUM
# iterate through string 
# define denotation * number of coins
# update  f' £total format setter

def end_of_day(till):
    total = 0 
    for money, count_of in till.items():
        if money == "1p":
            total += 0.01 * count_of
        elif money == "2p":
            total += 0.02 * count_of
        elif money == "5p":
            total += 0.05 * count_of
        elif money == "10p":
            total += 0.10 * count_of
        elif money == "20p":
            total += 0.20 * count_of
        elif money == "50p":
            total += 0.50 * count_of
        elif money == "£1":
            total += 1.00 * count_of
        elif money == "£2":
            total += 2.00 * count_of
        elif money == "£5":
            total += 5.00 * count_of
        elif money == "£10":
            total += 10.00 * count_of
        elif money == "£20":
            total += 20.00 * count_of
        elif money == "£50":
            total += 50.00 * count_of
    return f"£{total:.2f}"
        

     