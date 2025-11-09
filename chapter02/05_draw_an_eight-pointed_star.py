"""
Draw an eight-pointed star

Description:
Use the turtle library to draw an eight-pointed star (octagram-shaped figure)
similar to the sample output on the problem page.
"""

# draw_an_eight-pointed_star.py
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
