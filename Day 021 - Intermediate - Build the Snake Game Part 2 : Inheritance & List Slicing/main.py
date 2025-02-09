from turtle import Turtle, Screen, teleport
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("mediumseagreen")
screen.title("Snake Game")
screen.tracer(0) #Tracer is user to turn turtle animation on/off (on=1/off=0) and set delay for update drawings.

snake = Snake()
fruit = Food()
scoreboard = ScoreBoard()

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
    #detect collision with food.
    if snake.head.distance(fruit) < 25:
        scoreboard.Increased_Score()
        snake.extend()
        fruit.refresh()
    #detect collision with wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_on = False
        scoreboard.Game_Over()
    #detect collision with tail.
    for segment in snake.segments:
        # this condition is for snake.head to collision to itself to cause game over
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_on = False
            scoreboard.Game_Over()

screen.exitonclick()