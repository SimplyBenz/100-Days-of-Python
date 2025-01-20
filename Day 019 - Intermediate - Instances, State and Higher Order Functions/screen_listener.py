import turtle

screen = turtle.Screen()
timmy = turtle.Turtle()
timmy.shape("turtle")

def move_forward():
    timmy.forward(10)
    
def tilt_clockwise():
    timmy.right(10)

def tilt_counterclockwise():
    timmy.left(10)
    
def move_backward():
    timmy.back(10)    

def clear_screen():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()
    
screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(tilt_clockwise, "d")
screen.onkey(tilt_counterclockwise, "a")
screen.onkey(move_backward, "s")
screen.onkey(clear_screen,"c")

screen.exitonclick()