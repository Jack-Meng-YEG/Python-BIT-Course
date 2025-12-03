"""
Estimating pi with the Monte Carlo method

Use 123 as the random seed. Read an integer DARTS from input, then
randomly generate DARTS points inside a unit square. Count how many
points fall inside the quarter circle of radius 1 (x**2 + y**2 <= 1),
and use the ratio hits / DARTS to estimate pi:

    pi ≈ 4 * hits / DARTS

Output the estimated value of pi, formatted with 6 digits after
the decimal point.
"""

# estimate_pi.py
from random import random, seed
DARTS = eval(input())
seed(123)
hits = 0.0
for i in range(DARTS):
    x, y = random(), random()
    dist = pow(x ** 2 + y ** 2, 0.5)
    if dist <= 1.0:
        hits = hits + 1
pi = 4 * (hits/DARTS)
print("{:.6f}".format(pi))