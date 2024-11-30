from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_len=1.2,stretch_wid=1.2)
        self.penup()
        self.color("blue")
        self.speed("fastest")
        self.refresh()
    
    #Changes the location of the circle turtle using random   
    def refresh(self):
        random_x = random.randint(-380, 380)
        random_y = random.randint(-380, 380)
        self.goto(random_x,random_y)