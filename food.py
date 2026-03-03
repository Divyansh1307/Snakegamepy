from turtle import Turtle
from random import Random, randint


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.shapesize(0.5,0.5)
        self.speed("fastest")
        self.n_loc()
    def n_loc(self):
        x2= randint(-280,280)
        y2 = randint(-280,280)
        self.goto(x2,y2)





