from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time
screen=Screen()
food=Food()
scoreboard=ScoreBoard()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
snake=Snake(screen)
screen.listen()
screen.onkey(snake.up,"w")
screen.onkey(snake.left,"a")
screen.onkey(snake.down,"s")
screen.onkey(snake.right,"d")
screen.onkey(snake.up,"Up")
screen.onkey(snake.left,"Left")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
cont=True
while cont:
    snake.move()
    screen.update()
    time.sleep(0.1)
    if snake.snake.distance(food) < 18:
        scoreboard.inc()
        food.redo()
        snake.extend()
    if snake.snake.xcor()>280 or snake.snake.xcor()<-280 or snake.snake.ycor()>280 or snake.snake.ycor()<-280:
        cont=False
        scoreboard.end()
    many=(snake.connect())[1:]
    for segment in many:
        if snake.snake.distance(segment)<1:
            cont = False
            scoreboard.end()
screen.exitonclick()