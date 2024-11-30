import turtle as t
import colorgram
import random

artcolor=["blue","cyan","chocolate","DarkOrchid1","green","gold","red","magenta",'salmon']
# color=colorgram.extract("turtle/image.jpg",10)
# for colors in color:
#     r=colors.rgb.r
#     g=colors.rgb.g
#     b=colors.rgb.b
#     colorset=(r,g,b)
#     artcolor.append(colorset)

# print(artcolor)

t.colormode(225)
tim= t.Turtle()
tim.pensize(15)
tim.penup()
tim.speed("fastest")
n=0

def colorart():
        for j in range(10):
            tim.color(random.choice(artcolor))
            tim.dot()
            tim.forward(50)
                
def position_corrector():
    tim.backward(300)
    tim.right(90)
    tim.forward(150)
    tim.left(90)   

                
position_corrector()     
while n<10:
    colorart()
    tim.backward(50)
    tim.left(90)    
    tim.forward(50)
    tim.left(90)
    tim.forward(450)
    tim.left(180)
    n=n+1 
tim.hideturtle()    
    
    








screen=t.Screen()
screen.exitonclick()