from turtle import Turtle
class Snake():
    def __init__(self,screen):
        x = 0
        y = 0
        self.segments = []
        for i in range(0, 3):
            tim = Turtle()
            tim.penup()
            tim.shape("square")
            tim.color("white")
            tim.turtlesize(0.9)
            tim.goto(x-20, y)
            x = tim.xcor()
            y = tim.ycor()
            self.segments.append(tim)
        screen.update()
        self.snake=self.segments[0]
        self.snake.color("red")
    def move(self):
        x = self.snake.pos()[0]
        y = self.snake.pos()[1]
        self.snake.forward(20)
        for i in range(1, len(self.segments)):
            segment = self.segments[i]
            x2 = segment.pos()[0]
            y2 = segment.pos()[1]
            segment.goto(x, y)
            x = x2
            y = y2
    def extend(self):
        tim = Turtle()
        tim.penup()
        tim.shape("square")
        tim.color("white")
        tim.turtlesize(0.9)
        tim.goto(self.segments[-1].position())
        self.segments.append(tim)
    def connect(self):
        return self.segments
    def up(self):
        if self.snake.heading()!=270:
            self.snake.setheading(90)
    def down(self):
        if self.snake.heading() != 90:
            self.snake.setheading(270)
    def left(self):
        if self.snake.heading() != 0:
            self.snake.setheading(180)
    def right(self):
        if self.snake.heading() != 180:
            self.snake.setheading(0)