"""
Draw a windmill pattern using the turtle module.

Use the turtle library to draw a windmill shape in which each blade has an
interior angle of 45 degrees and a side length of 150 pixels.

Hint: The turtle.goto(x, y) function can move the turtle to the coordinate (x, y).
"""

# draw_a_windmill_pattern.py
import turtle as t
t.setup(800,800)
t.penup()
t.pensize(5)
t.pendown()
for i in range(4):
    t.fd(150)
    t.right(90)
    t.circle(-150,45)
    t.goto(0,0)
    t.left(45)
t.done()