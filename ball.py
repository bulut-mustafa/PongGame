from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color('white')
        self.x_move = 5
        self.y_move = 5
       

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)    
    
    def bounce(self):
        self.y_move *= -1
        
    def hit(self):
        self.x_move *= -1
    
    def resetpos(self):
        self.goto(0,0)
        self.hit()