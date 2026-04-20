from turtle import Turtle
class Player1(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.shape("square")
        self.color("white")
        self.shapesize(1,5)
        self.setheading(90)
        self.penup()
        self.speed("fastest")
        self.goto(-350,0)
        self.showturtle()
    def up(self):
        self.forward(20)
    def down(self):
        self.backward(20)