from turtle import Turtle
import random

class Food(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("square")
        # self.shape("circle")
        self.penup()
        # self.shapesize(0.5,0.5)
        self.color("black")
        self.speed("fastest") #because we don't want to see it move the fruit will create first before move it to random position
        self.refresh()
    
    def refresh(self):
        random_x = int(random.randint(-250,250))
        random_y = int(random.randint(-250,250))
        self.goto(random_x,random_y)