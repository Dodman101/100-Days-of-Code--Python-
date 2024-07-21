import turtle as t
import random

tim = t.Turtle()
# tim.shape("turtle")
# tim.color("red")
# tim.forward(100)
# tim.right(90)
#
# #Draw a square
# for _ in range(4):
#     tim.forward(100)
#     tim.left(90)

# Draw a dashed line
# for _ in range(15):
#     tim.forward(10)
#     tim.pendown()
#     tim.forward(10)
#     tim.penup()

# # Draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon and decagon

# colours = ["white smoke", "white smoke", "cyan", "light sea green", "light sea green", "light sea green", "gold", "green yellow", "orange red", "yellow"]

# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)

# for shape_side_n in range(3, 11):
#     tim.color(random.choice(colours))
#     draw_shape(shape_side_n)

# Generate random colours
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

# Random Walk
# cardinal_points = [0, 90, 180, 270]


# def random_walk():
#     tim.forward(30)
#     tim.speed("fastest")
#     tim.setheading(random.choice(cardinal_points))
#     tim.color(random_color())

# for _ in range(200):
#     tim.width(15)
#     random_walk()


# Draw a Spirograph

tim.speed("fastest")

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()
