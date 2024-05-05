# creating a spirograph that has random color for each circle

# importing modules for the code
import turtle as t
import random

tim = t.Turtle()
t.colormode(255)


# function that can select a random color
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


# setting the speed of the drawing
tim.speed("fastest")

"""function to create a spirograph"""


def draw_spirograph(size_of_gap):
    for i in range(int(360 / size_of_gap)):  # Range cannot be in float number
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(5)


screen = t.Screen()
screen.exitonclick()
