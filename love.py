import turtle
import math
screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(width=1200, height=900)
t = turtle.Turtle()
t.speed(0)
t.hideturtle()
t.penup()
t.color("#ffb6c1")
for scale in range(9, 16):
    for i in range(250):
        angle = i * (math.pi * 2) / 250
        x = 16 * (math.sin(angle) ** 3) * scale
        y = (13 * math.cos(angle) - 5 * math.cos(2 * angle) - 2 * math.cos(3 * angle) - math.cos(4 * angle)) * scale
        t.goto(x, y)
        t.write("LOVE", align="center", font=("Arial", 8,"bold"))
turtle.done()