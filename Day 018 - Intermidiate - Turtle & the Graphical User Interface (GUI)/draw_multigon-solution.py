from turtle import Turtle
from random import choice

timmy = Turtle()
timmy.shape("turtle")

colours = ["red", "green", "blue", "yellow", "purple", "orange", "pink", "black", "white", "cyan", "magenta", "brown"]

def draw_shape(num_sides):
    for _ in range(num_sides):
        timmy.forward(100)
        timmy.right(360 / num_sides)
        
for shape_side_n in range(3, 11):
    timmy.color(choice(colours))
    draw_shape(shape_side_n)