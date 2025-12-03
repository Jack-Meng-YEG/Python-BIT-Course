"""
Problem: Three-digit Armstrong (narcissistic) numbers.

A "3-digit Armstrong number" is a three-digit integer ABC such that

    A^3 + B^3 + C^3 = ABC

(where A, B and C are its hundreds, tens and units digits).

Write a program that finds all 3-digit Armstrong numbers between 100 and 999
and prints them in ascending order, separated by commas (e.g. 153, 370, 371, 407).
"""

# three_digit_armstrong_numbers.py
s = ""
for i in range(100, 1000):
    t = str(i)
    if pow(eval(t[0]),3) + pow(eval(t[1]),3) + pow(eval(t[2]),3) == i :
        s += "{},".format(i)
print(s[:-1])