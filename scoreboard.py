from turtle import Turtle
ALIGNMENT = "center"
FONT = ('courier', 14, 'bold')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.get_high_score()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 280)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, align= ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.set_high_score()
        self.score = 0
        self.update_scoreboard()

    def get_high_score(self):
        with open("data.txt") as file:
            self.high_score = int(file.read())

    def set_high_score(self):
        with open("data.txt", mode="w") as file:
            file.write(f"{self.high_score}")

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"GAME OVER", False, align= ALIGNMENT, font=FONT)

