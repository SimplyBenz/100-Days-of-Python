from turtle import Turtle, Screen
from random import randint

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

screen = Screen()
screen.setup(width=500, height=400)
screen.textinput(title="Make a guess", prompt="Which turtle will win")

StartPosX = -230
StartPostY = -100

for color in colors:
    timmy_ = Turtle(shape="turtle")
    timmy_.penup()
    timmy_.goto(StartPosX, StartPostY)
    timmy_.color("black",color)
    StartPostY += 40

while True:
    for timmy_ in screen.turtles():
        timmy_.forward(randint(0, 10))
        if timmy_.xcor() > 230:
            break

screen.exitonclick()


# 'Below thi is AI Generate suggestion'

# from turtle import Turtle, Screen
# from random import randint

# StartPosX = -230
# StartPostY = -100

# colors = ["red", "blue", "green", "yellow", "purple", "orange"]

# screen = Screen()

# turtles = []

# for color in colors:
#     timmy_ = Turtle(shape="turtle")
#     timmy_.penup()
#     timmy_.goto(StartPosX, StartPostY)
#     timmy_.color(color)
#     turtles.append(timmy_)
#     StartPostY += 40

# race_on = True

# while race_on:
#     for timmy_ in turtles:
#         timmy_.forward(randint(0, 10))
#         if timmy_.xcor() > 230:
#             race_on = False
#             break

# screen.exitonclick()