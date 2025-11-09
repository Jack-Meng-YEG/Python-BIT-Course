"""
Draw a regular octagon using the turtle module.

Description:
Use the turtle library to draw a regular octagon.
"""

# draw_a_regular_octagon.py
import turtle as t
t.setup(900,900)
t.penup()
t.pensize(5)
t.goto(-160,-350)
t.pendown()
for i in range(8):
    t.fd(300)
    t.left(45)
t.done()