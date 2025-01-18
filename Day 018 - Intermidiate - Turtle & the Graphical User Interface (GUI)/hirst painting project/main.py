# import colorgram

# # Provide the correct path to the image file
# image_path = '/Users/macbook/Code/100-Days-of-Python/Day 018 - Intermidiate - Turtle & the Graphical User Interface (GUI)/hirst painting project/image.jpg'
# colors = colorgram.extract(image_path, 14)

# # Extract and display RGB values
# # rgb_colors = [color.rgb for color in colors] <- this tuple have r= g= b= in code
# rgb_colors = [(color.rgb.r, color.rgb.g, color.rgb.b) for color in colors] # <- and this code is get lid of that r= g= b= and have only number in tuple

# print(rgb_colors)

# colors = [(254, 254, 254),
#           (172, 12, 40), 
#           (243, 231, 35), 
#           (187, 215, 252), 
#           (89, 165, 249), 
#           (252, 159, 225), 
#           (173, 31, 135), 
#           (70, 171, 103), 
#           (250, 98, 16), 
#           (64, 61, 162), 
#           (213, 233, 16), 
#           (251, 93, 1)]

import turtle 
import random

colors = [(172, 12, 40), 
          (243, 231, 35), 
          (187, 215, 252), 
          (89, 165, 249), 
          (252, 159, 225), 
          (173, 31, 135), 
          (70, 171, 103), 
          (250, 98, 16), 
          (64, 61, 162), 
          (213, 233, 16), 
          (251, 93, 1), 
          (247, 107, 37),]

timmy = turtle.Turtle()
turtle.colormode(255)



x_start = -225
y_start = -225

# for _ in range(10):
#     timmy.penup()
#     timmy.goto(XPos, YPos)
#     # random_color = random.choice(colors)
#     # timmy.dot(20, random_color)
#     timmy.dot(20, random.choice(colors))
#     XPos += 10
#     YPos += 10

for row in range(10):
    for col in range(10):
        timmy.hideturtle()
        timmy.penup()
        timmy.goto(x_start + col * 50, y_start + row * 50)
        timmy.dot(20, random.choice(colors))
        
turtle.done()