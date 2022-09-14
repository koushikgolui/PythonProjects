# import colorgram
# colors = colorgram.extract("image.jpg", 30)
#
# color_spec = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb = (r, g, b)
#     color_spec.append(rgb)
#
# print(color_spec)
import turtle
import turtle as t
import random


def random_colors():
    color_list = [(239, 236, 238), (238, 237, 236), (237, 237, 241), (26, 108, 164), (193, 38, 81), (237, 161, 50), (234, 215, 86), (227, 237, 229), (223, 137, 176), (143, 108, 57), (103, 197, 219), (21, 57, 132), (205, 166, 30), (213, 74, 91), (238, 89, 49), (142, 208, 227), (119, 191, 139), (5, 185, 177), (106, 108, 198), (137, 29, 72), (4, 162, 86), (98, 51, 36), (24, 155, 210), (229, 168, 185), (173, 185, 221), (29, 90, 95), (233, 173, 162), (156, 212, 190), (87, 46, 33), (37, 45, 83)]
    return random.choice(color_list)


tt = t.Turtle()
t.colormode(255)
position = tt.pos()
axis_x = -200
axis_y = -200
tt.penup()

for y in range(10):
    tt.setpos(axis_x, axis_y)
    for x in range(9):
        tt.color(random_colors())
        tt.dot(20)
        tt.forward(50)
    tt.dot(20)
    axis_y += 50


screen = t.Screen()
screen.exitonclick()
