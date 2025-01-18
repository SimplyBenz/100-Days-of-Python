import turtle
import random

turtle.speed("fastest")
timmy = turtle.Turtle()
turtle.colormode(255)

def random_color():
    """
    Generates a random color in the form of a hexadecimal string.
    """
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b) # Tuple of RGB values
    # print(random_color)
    return random_color

def risograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.seth(timmy.heading() + size_of_gap)
        

risograph(10)
