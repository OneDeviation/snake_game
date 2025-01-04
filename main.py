from turtle import Screen
import time
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("SNAKE")
screen.tracer(0)

def game_start():
    snake = Snake()
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")
    screen.onkey(snake.grow_tail, "G")

    game_is_on = True
    screen.update()
    while game_is_on:
        screen.update()
        time.sleep(.1)
        snake.move()
game_start()


# TODO: Create snake food
# TODO: Collision work
    # TODO: Detect collision with food
        # TODO: Scoreboard
    # TODO: Detect wall collision
    # TODO: Detect collision with tail

screen.exitonclick()
