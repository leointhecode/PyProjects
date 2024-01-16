import turtle as t
import colorgram as c
import random as r


def get_color(image, number_of_colors):
    colors = c.extract(image, number_of_colors)
    color_rgb = []
    for color in colors:
        rgb = color.rgb
        color_rgb.append(rgb[0:3])
    return color_rgb


waifu = t.Turtle()
waifu.ht()
t.colormode(255)
palette = get_color('tsukii.png', 6)

print(palette)
waifu.speed("fastest")
waifu.pu()
waifu.setheading(225)
waifu.forward(160)
waifu.setheading(0)

for i in range(10):
    for n in range(10):
        waifu.color(r.choice(palette))
        waifu.dot(13)
        waifu.pu()
        waifu.forward(25)

    waifu.back(250)
    waifu.left(90)
    waifu.forward(25)
    waifu.right(90)

screen = t.Screen()
screen.exitonclick()
