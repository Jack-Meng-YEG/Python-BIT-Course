"""
Draw an octagonal figure

Description:
Use the turtle library to draw an eight-pointed figure.
"""

# draw_an_octagonal_figure.py
import turtle as t
t.setup(900,900)
t.penup()
t.pensize(5)
t.goto(-250,-100)
t.pendown()
for i in range(8):
    t.fd(500)
    t.left(135)
t.done()