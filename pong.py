from turtle import Turtle


class Pong(Turtle):
    def __init__(self, positionx, positiony):
        super().__init__()
        self.create_pong(positionx, positiony)

    def create_pong(self, positionx, positiony):
        self.shape("square")
        self.penup()
        self.left(90)
        self.turtlesize(stretch_len=5)
        self.color("white")
        self.goto(x=positionx, y=positiony)

    def move_up(self):
        self.forward(20)

    def move_down(self):
        self.back(20)
