"""
Using the pow() function in Python.

Starting from a base value of 1.0, suppose a quantity changes by 0.1% each day
over one year (365 days):

1. Use pow() to calculate the final value if it increases by 0.1% per day.
2. Use pow() to calculate the final value if it decreases by 0.1% per day.
3. Print both results with two decimal places.
"""

# using_the_pow()_function.py
up=pow(1+0.001,365)
down=pow(1-0.001,365)
print("up:{:.2f}\ndown:{:.2f}".format(up,down))