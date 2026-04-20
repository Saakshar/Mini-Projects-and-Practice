from turtle import Turtle
import random
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.speed("fastest")
        self.penup()
        self.goto(20,0)
        self.shape("circle")
        self.color("white")
        self.showturtle()
        self.direction=0
        self.direction2=90
    def move(self):
        self.setheading(self.direction)
        self.forward(9)
        self.setheading(self.direction2)
        self.forward(5)
    def soft_bounce(self):
        self.direction2 += 180
        if self.direction2 == 470:
            self.direction2 -= 360
    def bounce(self):
        self.direction+=180
        if self.direction==360:
            self.direction-=360
        chance=random.randint(0,7)
        if chance>4:
            self.direction2 += 180
        if self.direction2 == 470:
            self.direction2 -= 360
    def reset(self):
        self.goto(0,0)