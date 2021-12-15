import random
import time
from turtle import Screen, Turtle

scr = Screen()
scr.setup(width=600, height=600)
scr.bgcolor('black')
scr.title('Snake Game')
scr.tracer(0)

START_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DIST = 20

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake(object):

    def __init__(self) -> None:
        self.segments: list[Turtle] = list()
        self.create_snake()

    @property
    def head(self):
        return self.segments[0]

    def create_snake(self):
        for pos in START_POS:
            self.add_seg(pos)

    def extend(self):
        self.add_seg(self.segments[-1].pos())

    def add_seg(self, pos):
        t = Turtle(shape='square')
        t.color('white')
        t.penup()
        t.setpos(pos)
        self.segments.append(t)

    def move(self):
        for index in range(len(self.segments) - 1, 0, -1):
            self.segments[index].setpos(
                self.segments[index - 1].pos()
            )
        self.head.fd(MOVE_DIST)

    def up(self):
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(UP)

    def down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(DOWN)

    def left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(LEFT)

    def right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(RIGHT)


class Food(Turtle):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('blue')
        self.speed('fastest')
        self.set_rand_pos()

    def set_rand_pos(self):
        while True:
            new_x = random.randint(-280, 280)
            new_y = random.randint(-280, 280)
            if (new_x, new_y) != self.pos():
                self.goto(new_x, new_y)
                break


class ScoreBoard(Turtle):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.color('white')
        self.setpos(0, 280)
        self.hideturtle()
        self.val = -1
        self.text = ''
        self.update_add_one()

    def update_add_one(self):
        self.clear()
        self.val += 1
        self.text = f'Score: {self.val}'
        self.write(self.text, move=False, align='center',
                   font=('Cascadia code', 8, 'normal'))

    def game_over(self):
        self.setpos(0, 0)
        self.write('Game Over!')


snake = Snake()
food = Food()
sc_board = ScoreBoard()

scr.listen()
scr.onkey(snake.up, 'Up')
scr.onkey(snake.down, 'Down')
scr.onkey(snake.left, 'Left')
scr.onkey(snake.right, 'Right')

game_is_on = True
while game_is_on:
    scr.update()
    time.sleep(0.13)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.set_rand_pos()
        sc_board.update_add_one()
        snake.extend()

    # Detect collision with wall
    if not (-290 < snake.head.xcor() < 290) or not (-290 < snake.head.ycor() < 290):
        sc_board.game_over()
        game_is_on = False

    # Detect collision with tail
    for seg in snake.segments[1:]:
        if snake.head.distance(seg) < 10:
            game_is_on = False
            sc_board.game_over()

scr.exitonclick()
