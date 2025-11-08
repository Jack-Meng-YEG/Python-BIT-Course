"""
Draw an overlapping polygon using the turtle module.

Requirements:
1. Use the turtle module to draw a polygon in which each interior angle is 100 degrees.
2. The figure should be drawn as one continuous path that eventually returns to the starting point.
"""

# draw_an_overlapping_polygon.py
import turtle as t
t.setup(900,900)
t.penup()
t.pensize(5)
t.goto(-200,-200)
t.pendown()
for i in range(9):
    t.fd(400)
    t.left(80)
t.done()