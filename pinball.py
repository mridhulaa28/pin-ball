import turtle
import random

def start_game():
    global score, game_over
    score = 0
    score_display.clear()
    score_display.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))
    ball.goto(0, 0)
    ball.dx = 0.02
    ball.dy = -0.02
    game_over = False
    screen.update()

def game_over_screen():
    score_display.clear()
    score_display.goto(0, 0)
    score_display.write("Game Over!\nScore: {}\nPress 'R' to Restart".format(score), align="center", font=("Courier", 24, "normal"))
    score_display.goto(0, 260)

def restart_game():
    if game_over:
        start_game()

def choose_new_color(current_color):
    new_color = current_color
    while new_color == current_color:
        new_color = random.choice(ball_colors)
    return new_color


screen = turtle.Screen()
screen.title("Pinball Game")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

border_color = "yellow"
screen.bgcolor("black")

top_border = turtle.Turtle()
top_border.speed(0)
top_border.color(border_color)
top_border.penup()
top_border.goto(-400, 300)
top_border.pendown()
top_border.goto(400, 300)
top_border.hideturtle()

bottom_border = turtle.Turtle()
bottom_border.speed(0)
bottom_border.color(border_color)
bottom_border.penup()
bottom_border.goto(-400, -300)
bottom_border.pendown()
bottom_border.goto(400, -300)
bottom_border.hideturtle()

left_border = turtle.Turtle()
left_border.speed(0)
left_border.color(border_color)
left_border.penup()
left_border.goto(-400, 300)
left_border.pendown()
left_border.goto(-400, -300)
left_border.hideturtle()

right_border = turtle.Turtle()
right_border.speed(0)
right_border.color(border_color)
right_border.penup()
right_border.goto(400, 300)
right_border.pendown()
right_border.goto(400, -300)
right_border.hideturtle()

paddle = turtle.Turtle()
paddle.speed(0)
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=3)
paddle.penup()
paddle.goto(0, -280)

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.04
ball.dy = -0.04

score = 0
game_over = False

score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))

def move_left():
    x = paddle.xcor()
    if x > -350:
        x -= 20
        paddle.setx(x)

def move_right():
    x = paddle.xcor()
    if x < 350:
        x += 20
        paddle.setx(x)

screen.listen()
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")
screen.onkeypress(restart_game, "r")

ball_colors = ["red", "green", "blue", "yellow", "purple", "orange"]

while True:
    screen.update()

    if not game_over:
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        if ball.xcor() > 390 or ball.xcor() < -390:
            ball.dx *= -1

        if ball.ycor() > 290:
            ball.sety(290)
            ball.dy *= -1

        if ball.ycor() < -290:
            game_over = True
            game_over_screen()

        if ball.ycor() < -270 and paddle.xcor() - 50 < ball.xcor() < paddle.xcor() + 50:
            if ball.ycor() > -260:
                ball.sety(-260)
                ball.dy *= -1
            else:
                ball.dy *= -1

            if ball.xcor() < paddle.xcor() - 50 or ball.xcor() > paddle.xcor() + 50:
                ball.dx *= -1

            ball.color(choose_new_color(ball.color()))
            ball.dx *= 1.3
            ball.dy *= 1.3

            score += 10
            score_display.clear()
            score_display.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))
            
    else:
        pass
