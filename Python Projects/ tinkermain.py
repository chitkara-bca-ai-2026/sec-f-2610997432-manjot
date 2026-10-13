import math
import turtle

screen = turtle.Screen()
screen.setup(width=800, height=800)
screen.bgcolor("black")
screen.title("Beating Heart")
screen.tracer(0)  # Enables fast instant rendering

t = turtle.Turtle()
t.hideturtle()
t.color("#ffb6c1")
t.pensize(2)


def draw_heart(scale):
    t.clear()
    t.penup()

    for i in range(150):
        angle = i * (math.pi * 2) / 150
        x = 16 * (math.sin(angle) ** 3) * scale
        y = (
            13 * math.cos(angle)
            - 5 * math.cos(2 * angle)
            - 2 * math.cos(3 * angle)
            - math.cos(4 * angle)
        ) * scale

        if i == 0:
            t.goto(x, y)
            t.pendown()
        else:
            t.goto(x, y)

    t.penup()
    screen.update()


# Animation loop
scale = 12
growing = True

while True:
    draw_heart(scale)

    if growing:
        scale += 0.15
        if scale >= 15:
            growing = False
    else:
        scale -= 0.15
        if scale <= 12:
            growing = True
