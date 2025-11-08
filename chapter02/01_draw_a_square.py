"""
Draw a square using the turtle module.

Requirements:
1. Create an 800x800 pixel drawing window.
2. Set the line width to 5 pixels.
3. Draw a 400x400 pixel square. The square should be centered on the canvas.
4. When the square is finished, keep the window open.
"""

# draw_a_square.py
import turtle as t
t.setup(800,800)
t.pensize(5)
t.penup()
t.goto(-200,-200)
t.pendown()
for i in range(4):
    t.fd(400)
    t.left(90)
t.done()
