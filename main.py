import turtle

import colorgram
from turtle import Turtle, Screen
import random

rgb_colors = []  # creating a list to store a tuple() for RGB colors
# Below code is for extracting colors from the list and storing it in the list in tuples form written by me:
colors_extracted = colorgram.extract('hirst.jpg', 30)
for n in range (30):
    first_color = colors_extracted[n]
    # print(first_color.rgb[0:3])
    rgb_colors.append(first_color.rgb[0:3])

# Below code is for extracting colors from the list and storing it in the list in tuples form written by YU:
colors_extracted = colorgram.extract('hirst.jpg', 30)
for colors in colors_extracted:
    r = colors.rgb.r
    g = colors.rgb.g
    b = colors.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

print(rgb_colors)

color_list = [(249, 228, 17), (213, 13, 9), (198, 12, 35), (231, 228, 5), (197, 69, 20), (33, 90, 188), (43, 212, 71), (234, 148, 40), (33, 30, 152), (16, 22, 55), (66, 9, 49), (240, 245, 251), (244, 39, 149), (65, 202, 229), (14, 205, 222), (63, 21, 10), (224, 19, 111), (229, 165, 8), (15, 154, 22), (245, 58, 16), (98, 75, 9), (248, 11, 9), (222, 140, 203), (68, 240, 161), (10, 97, 62), (5, 38, 33), (68, 219, 155)]
turtle = Turtle()
screen = Screen()
screen.colormode(255)
is_on = True
x = -200
y = -200
def color_filling():
    for _ in range(8):
        turtle.color(random.choice(color_list))
        turtle.speed("fastest")
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(10)
        turtle.end_fill()
        turtle.penup()
        turtle.forward(60)


while is_on:
    if y != 300:
        turtle.penup()
        turtle.hideturtle()
        turtle.goto(x, y)
        color_filling()
        y += 50
    else:
        is_on = False
