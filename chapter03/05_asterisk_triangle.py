"""
Problem: Asterisk Triangle

Read an odd integer N. Print an isosceles triangle made of asterisks:
rows contain 1, 3, 5, …, N asterisks. Each row is centered within width N
(using spaces).

Input:
    An odd integer N
Output:
    (N+1)//2 lines forming the triangle

Example
Input:
    3
Output:
     *
    ***
"""

# asterisk_triangle.py
n = eval(input())
for i in range(1,n+1,2):
    print("{0:^{1}}".format('*'*i, n))