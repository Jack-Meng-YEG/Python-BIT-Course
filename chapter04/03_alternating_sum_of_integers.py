"""
Problem: Alternating sum of integers.

Write a program to compute the value of the series

    1 - 2 + 3 - 4 + ... - 966

All terms are integers starting from 1 and increasing by 1 each time.
Odd numbers are added (positive sign) and even numbers are subtracted
(negative sign). Print the final sum.
"""

# alternating_sum_of_integers.py
s = 0
count = 1
while count <=966:
    if count%2 == 0:
        s -= count
    else:
        s += count
    count += 1
print(s)