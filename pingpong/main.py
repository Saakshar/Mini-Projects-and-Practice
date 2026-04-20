from turtle import Screen,Turtle
from p1controls import Player1
from p2controls import Player2
from ball import Ball
import time
screen=Screen()
screen.bgcolor("black")
screen.setup(800,600)
screen.title("Ping Pong")
screen.listen()
screen.tracer(0)
p1_score=0
p2_score=0
scoreboard=Turtle()
scoreboard.speed("fastest")
scoreboard.penup()
scoreboard.hideturtle()
scoreboard.goto(20,280)
scoreboard.color("white")
scoreboard.write(f"Player 1 Score: {p1_score} Player 2 Score: {p2_score}",align="center")
p1=Player1()
p2=Player2()
ball=Ball()
screen.update()
screen.onkeypress(p1.up,"w")
screen.onkeypress(p1.down,"s")
screen.onkeypress(p2.up,"Up")
screen.onkeypress(p2.down,"Down")
time.sleep(1)
cont=True
while cont:
    ball.move()
    screen.update()
    time.sleep(0.03)
    if ball.xcor() > 390:
        p1_score+=1
        scoreboard.clear()
        scoreboard.write(f"Player 1 Score: {p1_score} Player 2 Score: {p2_score}", align="center")
        ball.reset()
    elif ball.xcor() < -390:
        p2_score+=1
        scoreboard.clear()
        scoreboard.write(f"Player 1 Score: {p1_score} Player 2 Score: {p2_score}", align="center")
        ball.reset()
    elif ball.ycor()>290 or ball.ycor()<-290:
        ball.soft_bounce()
    elif ball.distance(p1)<50 and ball.xcor()<-340:
        ball.bounce()
    elif ball.distance(p2)<50 and ball.xcor()>340:
        ball.bounce()
screen.exitonclick()