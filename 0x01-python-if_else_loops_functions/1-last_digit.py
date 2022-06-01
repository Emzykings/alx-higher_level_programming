#!/usr/bin/python3

import random

number = random.randint(-10000, 10000)

1_digit = 0

if number >= 0:

1_digit = number % 10

else:

1_digit = (number % 10) - 10

if 1_digit > 5:

print(f"Last digit of {number:d} is {l_digit:d} and is greater than 5")

elif 1_digit == 0:

print(f"Last digit of {number:d} is {l_digit:d} and is 0")

else:

print(f"Last digit of {number:d} is {l_digit:d}",

"and is less than 6 and not 0")
