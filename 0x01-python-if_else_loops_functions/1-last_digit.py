#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
Last_digit = abs(number) % 10
print("Last digit of {} is {} and is ".format(number, Last_digit), end="")
if Last_digit > 5:
    print("greater than 5")
elif Last_digit == 0:
    print("0")
elif Last_digit < 6 and Last_digit > 0:
    print("less than 6 and not 0")
