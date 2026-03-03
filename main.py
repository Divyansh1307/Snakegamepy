from turtle import  Screen ,Turtle

import time
from snake import Snake
from food import Food
from scr import Scr
sc = Screen()
sc.bgcolor("black")
sc.setup(600,650)
sc.title("my snake game")
wall = Turtle()
wall.color("pink")
wall.penup()
wall.speed(1000)
wall.goto(285,285)
wall.pendown()
wall.rt(90)
wall.goto(285,-285)
wall.rt(90)
wall.goto(-285,-285)
wall.rt(90)
wall.goto(-285,285)
wall.rt(90)
wall.goto(285,285)
wall.hideturtle()

# # with the help of variables
# n=3
# xcor=0
# ycor=0
# for i in range (n):
#
#     timmy = Turtle(shape="square")
#     timmy.penup()
#     timmy.color("red")
#     timmy.goto(xcor,ycor)
#     xcor-= -20
#     snake.append(timmy)
## with the help of tuple
sc.tracer(0)
saap = Snake()
khaana= Food()
scr=Scr()
sc.listen()
sc.onkey(saap.up,"Up")
sc.onkey(saap.down,"Down")
sc.onkey(saap.left,"Left")
sc.onkey(saap.right,"Right")

kk=True
while kk:
    sc.update()
    time.sleep(0.1)
    saap.move()
    if saap.head.distance(khaana) < 15:
        khaana.n_loc()
        scr.up()
        saap.ext()
    if saap.head.xcor() > 280 or saap.head.xcor() < -280 or saap.head.ycor() > 280 or saap.head.ycor() <-280:
        kk = False
        scr.gameover()

    for j in saap.snake[1:]:
        if saap.head.distance(j) <10 :
            kk = False
            scr.gameover()










sc.exitonclick()
# 3 sq
