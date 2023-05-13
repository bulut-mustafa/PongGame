from turtle import Turtle

class Paddle(Turtle):
    
    def __init__(self,xcor, ycor):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(5,1)
        self.penup()
        self.goto(xcor, ycor)
    
    
    def up(self):
        self.goto(self.xcor(), self.ycor()+40)
    
    def down(self):
        self.goto(self.xcor(), self.ycor()-40)

    
        