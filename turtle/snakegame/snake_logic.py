from turtle import Turtle
 
 #constant
STARTING_POSITION=[(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE=20
UP=90
DOWN=270
LEFT=180
RIGHT=0

class Snake:
    def __init__(self):
        self.segment=[]
        self.create_snake()
        self.head=self.segment[0]
        self.x=0
        self.y=0

    #Creating the starting snake
    def create_snake(self):
        for position in STARTING_POSITION:
            if position==(0,0):
                tur=Turtle(shape="turtle")
                tur.penup()
                tur.goto(position)
                tur.color('white')
                tur.pensize(15)
                self.segment.append(tur)
            tur=Turtle(shape="square")
            tur.penup()
            tur.goto(position)
            tur.color('white')
            tur.pensize(10)
            self.segment.append(tur)
      
      
    #For the movement of the snake        
    def move(self):
        for i in range(len(self.segment)-1,0,-1):
            new_x=self.segment[i-1].xcor()
            new_y=self.segment[i-1].ycor()
            self.segment[i].goto(new_x,new_y)
        self.x=new_x
        self.y=new_y  
        self.head.forward(MOVE_DISTANCE)        
    
    #Move up   
    def up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)
    #Move down    
    def down(self):
         if self.head.heading()!=UP:
            self.head.setheading(DOWN)
    
    #Move left    
    def left(self):
         if self.head.heading()!=RIGHT:
            self.head.setheading(LEFT)    
    
    #Move right   
    def right(self):
         if self.head.heading()!=LEFT:
            self.head.setheading(RIGHT) 
    
    #Extend the tail        
    def add_new_segment(self):
        new_segment=Turtle(shape="square")   
        new_segment.penup()
        new_segment.color('white')
        new_segment.pensize(10)
        new_segment.goto(self.x,self.y)
        self.segment.append(new_segment)
        
    def resetSnake(self): 
        for segment in self.segment:
            segment.goto(1000,1000)
        self.segment.clear()    
        self.create_snake()      
        self.head=self.segment[0]
            
             