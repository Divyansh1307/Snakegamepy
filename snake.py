from turtle import Turtle

FONT = ('Courier', 26, 'normal')
ALIGN = "center"
class Scr(Turtle):
    def __init__(self):
        super().__init__()
        self.color("green")
        self.hideturtle()
        self.penup()
        self.goto(0,300)


        self.curr=0
        self.score()
    def score(self):
        self.write(f"score:{self.curr}", move=False, align=ALIGN, font=FONT)
    def up(self):
        self.curr+=1
        self.clear()
        self.score()
    def gameover(self):
        self.goto(0,0)



        self.write(f"game over final score:{self.curr}", move=False, align=ALIGN, font=FONT)



