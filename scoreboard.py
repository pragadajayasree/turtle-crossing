from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.lev_el()

    def lev_el(self):
        self.clear()
        self.penup()
        self.hideturtle()
        self.goto(x=-290, y=260)
        self.update()

    def update(self):
        self.clear()
        self.write(f"Level:{self.level}",align="left", font=FONT)

    def inc(self):
        self.level += 1
        self.update()

    def over(self):
        self.home()
        self.write("game over", align="center", font=FONT  )


