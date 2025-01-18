# from turtle import Turtle

# timmy = Turtle()
# timmy.shape("turtle")

# for i in range(3, 360):
#     for _ in range(i):
#         timmy.forward(100)
#         if i % 2 == 0:
#             timmy.right(360 / i)
#         else:
#             timmy.left(360 / i)

from turtle import Turtle
from random import randint

timmy = Turtle()
timmy.shape("turtle")

def draw_shape(num_sides):
    for _ in range(num_sides):
        timmy.forward(100)
        timmy.right(360 / num_sides)
        
for shape_side_n in range(3, 11):
    # print(f"{randint(0, 255):02x}")
    timmy.color(f"#{randint(0, 255):02x}{randint(0, 255):02x}{randint(0, 255):02x}")
    draw_shape(shape_side_n)