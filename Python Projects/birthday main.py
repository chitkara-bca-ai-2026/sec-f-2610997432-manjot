import math
import turtle

screen = turtle.Screen()
screen.bgcolor("black")
screen.tracer(0)

t = turtle.Turtle()
t.hideturtle()
t.penup()
t.color("#ffb6c1")


def draw_heart(scale_offset):
    t.clear()
    for scale in range(11, 17):
        current_scale = scale + scale_offset
        for i in range(100):
            angle = i * (math.pi * 2) / 100
            x = 16 * (math.sin(angle) ** 3) * current_scale
            y = (
                13 * math.cos(angle)
                - 5 * math.cos(2 * angle)
                - 2 * math.cos(3 * angle)
                - math.cos(4 * angle)
            ) * current_scale

            t.goto(x, y)
            t.write("I love you", align="center", font=("Arial", 1, "bold"))

    screen.update()


def animate():
    global scale_offset, growing

    draw_heart(scale_offset)

    if growing:
        scale_offset += 0.15
        if scale_offset >= 1.5:
            growing = False
    else:
        scale_offset -= 0.15
        if scale_offset <= 0:  # Fixed: comparison operation instead of single '='
            growing = True

    screen.ontimer(animate, 30)


# Initial state setup
scale_offset = 0
growing = True

# Start animation
animate()
turtle.done()

         