import random
import turtle

def random_walk_turtle(steps):
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
    walker.shape("turtle")
    walker.pensize(1)
    walker.speed(0)  # Set the fastest drawing speed
    walker.penup()
    walker.goto(0, 0)
    walker.pendown()

    # Perform the random walk
    for _ in range(steps):
        walker.color(f"#{random.randint(0, 255):02x}{random.randint(0, 255):02x}{random.randint(0, 255):02x}")
        # direction = random.choice(['N','NE','E','SE','S','SW','W','NW'])
        direction = random.choice(['NE','SE','SW','NW'])
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
        
        walker.forward(4)  # Move forward by a fixed step size

    # Finish
    walker.hideturtle()
    screen.mainloop()

# Example usage
random_walk_turtle(steps=10000)
