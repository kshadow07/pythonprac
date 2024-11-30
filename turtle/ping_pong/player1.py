from turtle import Turtle

class Player1(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=2)
        self.penup()
        self.goto(-430, 0)
        self.speed("fastest")
        
    def up(self):
        if self.ycor()>340:
            new_y = self.ycor()
            self.goto(self.xcor(), new_y)
        else:
           new_y = self.ycor() + 75
           self.goto(self.xcor(), new_y) 
           
    def down(self):
         if self.ycor()<-340:
            new_y = self.ycor()
            self.goto(self.xcor(), new_y)
         else:
            new_y = self.ycor() - 75
            self.goto(self.xcor(), new_y)        