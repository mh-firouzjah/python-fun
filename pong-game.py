from turtle import Screen, Turtle
from typing import List

scr = Screen()
scr.setup(width=800, height=500)
scr.bgcolor('black')
scr.title('Pong Game')


# scr.tracer(0)


def draw_middle():
    line = Turtle()
    line.hideturtle()
    line.color('white')
    line.penup()
    for i in range(-250, 250, 30):
        line.setpos(0, i)
        line.pendown()
        line.setpos(0, i + 10)
        line.penup()


draw_middle()


class Board(Turtle):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.color('white ')


scr.exitonclick()
