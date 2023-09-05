#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if (number >= 0):
    new = number % 10
else:
    new = (-1 * number) % 10
    new *= -1
if (new > 5):
    print("Last digit of", number , f"is {new:.0f} and is greater than 5")
if (new == 0):
    print("Last digit of", number , f"is {new:.0f} and is 0")
if (new < 6 and not(new == 0)):
    print("Last digit of", number , f"is {new:.0f} and is less than 6 and not 0")
