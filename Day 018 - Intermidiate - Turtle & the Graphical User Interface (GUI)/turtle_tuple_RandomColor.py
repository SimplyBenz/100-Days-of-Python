import random
import turtle

def random_color():
    """
    Generates a random color in the form of a hexadecimal string.
    """
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b) # Tuple of RGB values
    print(random_color)
    return random_color

def random_walk_turtle(steps=100):
    """
    Simulates a 2D random walk and visualizes it using the turtle module.
    
    Parameters:
    steps (int): Number of steps in the random walk.
    """
    # Set up the turtle screen
    screen = turtle.Screen()
    screen.setup(width=800, height=800)
    screen.title("2D Random Walk - Turtle Visualization")
    screen.bgcolor("white")

    # Set up the turtle
    walker = turtle.Turtle()
    turtle.colormode(255)  # Set the color mode to RGB
    walker.shape("turtle")
    walker.pensize(8)
    walker.speed(0)  # Set the fastest drawing speed
    walker.penup()
    walker.goto(0, 0)
    walker.pendown()

    # Perform the random walk
    for _ in range(steps):
        walker.color(random_color())
        direction = random.choice(['N','NE','E','SE','S','SW','W','NW'])
        if direction == 'N':
            walker.setheading(90)  # Point up
        elif direction == 'S':
            walker.setheading(270)  # Point down
        elif direction == 'W':
            walker.setheading(180)  # Point left
        elif direction == 'E':
            walker.setheading(0)  # Point right
        elif direction == 'NE':
            walker.setheading(45)
        elif direction == 'SE':
            walker.setheading(315)
        elif direction == 'SW':
            walker.setheading(225)
        elif direction == 'NW':
            walker.setheading(135)
        
        walker.forward(20)  # Move forward by a fixed step size

    # Finish
    walker.hideturtle()
    screen.mainloop()

# Example usage
random_walk_turtle(steps=1000)
