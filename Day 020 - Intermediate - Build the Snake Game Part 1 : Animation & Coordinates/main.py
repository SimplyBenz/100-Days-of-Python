from turtle import Turtle, Screen, teleport
import time
import snake

screen = Screen()
screen.setup(width=800,height=800)
screen.bgcolor("mediumseagreen")
screen.title("Snake Game")
screen.tracer(0) #Tracer is user to turn turtle animation on/off (on=1/off=0) and set delay for update drawings.

snake = snake.Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    
    snake.move()

screen.exitonclick()