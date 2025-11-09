"""
Draw a Python snake.

This is a practice example corresponding to the in-class demonstration.
Use the turtle library to draw a snake-shaped curve similar to the sample
shown in the online course for Chapter 02.
"""

# draw_a_python_snake.py
import turtle as t
t.setup(1200,800)
t.penup()
t.pensize(35)
t.pencolor("purple")
t.goto(-400,0)
t.pendown()
t.seth(-40)
for i in range(4):
	t.circle(60,80)
	t.circle(-60,80)
t.circle(60,80/2)
t.fd(60)
t.circle(45,180)
t.fd(50)
t.done()