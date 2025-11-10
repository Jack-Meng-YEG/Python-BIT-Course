"""
Using the pow() function in Python.

Starting from a base value of 1.0, suppose a quantity changes by 1% each day
over one year (365 days):

1. Use pow() to calculate the final value if it increases by 1% per day.
2. Use pow() to calculate the final value if it decreases by 1% per day.
3. Print both results with two decimal places.
"""

# using_the_pow()_function.py
print("increase:{:.2f}\ndecrease:{:.2f}".format(pow(1+0.01,365),pow(1-0.01,365)))