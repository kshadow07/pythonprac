from asyncio import futures
from turtle import Turtle, position
import random

class Car(Turtle):
    def __init__(self) :
        super().__init__()
        self.shape("square")
        self.color("black")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.goto(0,0)
        self.speed("fastest")
        self.move()
    
        
    def move(self):
        self.backward(random.randint(30,60))