from turtle import Turtle

timmy = Turtle()
timmy.shape("turtle")

for _ in range(4):
    timmy.right(90)
    timmy.forward(100)

timmy.screen.exitonclick()