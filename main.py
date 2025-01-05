from turtle import Screen
import time

from scoreboard import Scoreboard
from snake import Snake
from food import Food

screen = Screen()
screen.setup(width=610, height=610)
screen.bgcolor("black")
screen.title("SNAKE")
screen.tracer(0)

def game_start():
    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")
    screen.onkey(snake.grow_tail, "G")

    game_is_on = True
    #Move the snake
    while game_is_on:
        screen.update()
        time.sleep(.1)
        snake.move()

        #detect collision with food
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.grow_tail()
            scoreboard.increase_score()

    #Detect wall collision
        if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
            game_is_on = False
            scoreboard.game_over()

    #Detect collision with tail
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                game_is_on = False
                scoreboard.game_over()

game_start()




screen.exitonclick()
