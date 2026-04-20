from turtle import Turtle
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.pencolor("white")
        self.penup()
        self.pensize(10)
        self.hideturtle()
        self.goto(0,272)
        self.write(f"Score: {self.score}", align="center",font=('Arial', 18, 'normal'))
    def inc(self):
        self.score+=1
        self.clear()
        self.write(f"Score: {self.score}", align="center",font=('Arial', 18, 'normal'))
    def end(self):
        self.goto(0,0)
        self.write("Game Over", align="center", font=('Arial', 28, 'normal'))