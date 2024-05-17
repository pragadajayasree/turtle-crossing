from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.create()

    def create(self):
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def move(self):
        self.forward(MOVE_DISTANCE)

    def is_reached(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        return False

    def reposition(self):
        self.goto(STARTING_POSITION)



