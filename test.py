'''
test base
'''
import turtle
from random import randint as rit

turtle.colormode(255)
scr = turtle.Screen()

tim = turtle.Turtle()

# tim.penup()
# tim.goto(-10, 200)
# tim.pendown()


def colors(): return rit(0, 255), rit(0, 255), rit(0, 255)

# for i in range(3, 13):
# tim.color(colors())
#     for _ in range(i):
#         tim.fd(100)
#         tim.right(360/i)


tim.speed('fastest')
for _ in range(360//10):
    tim.color(colors())
    tim.circle(100)
    tim.setheading(tim.heading()+10)

scr.exitonclick()
