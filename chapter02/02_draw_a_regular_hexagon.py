"""
Draw a regular hexagon using the turtle module.

Requirements:
1. Create a 900x900 pixel drawing window.
2. Set the line width to 5 pixels.
3. Draw a regular hexagon whose side length is 400 pixels. The hexagon
   should be centered on the canvas.
4. When the hexagon is finished, keep the window open.
"""

# draw_a_regular_hexagon.py
import turtle as t
t.setup(900,900)
t.penup()
t.pensize(5)
t.goto(-200,-346.41)
t.pendown()
for i in range(6):
    t.fd(400)
    t.left(60)
t.done()