from turtle import Turtle

timmy = Turtle()
timmy.shape("turtle")

for _ in range(15):
    timmy.penup()
    timmy.forward(10)
    timmy.pendown()
    timmy.forward(10)

timmy.screen.exitonclick()