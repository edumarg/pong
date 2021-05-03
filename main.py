# Simple Pong in Python 3

import turtle

window = turtle.Screen()
window.title("PONG")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)  # Stops the window from updating
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)  # Speed of animation
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.color("white")
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)  # Speed of animation
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.color("white")
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)  # Speed of animation
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.05
ball.dy = 0.05


# Move paddles
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    if y > 200:
        y = 200
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    if y < -200:
        y = -200
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    if y > 200:
        y = 200
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    if y < -200:
        y = -200
    paddle_b.sety(y)


# Keyboard binding
window.listen()
window.onkey(paddle_a_up, "w")
window.onkey(paddle_a_down, "s")
window.onkey(paddle_b_up, "i")
window.onkey(paddle_b_down, "k")

# Main game loop
while True:
    window.update()

    # Move ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # ball y movement
    if ball.ycor() >= 290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() <= -290:
        ball.sety(-290)
        ball.dy *= -1

    # ball x movement
    if ball.xcor() >= 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
    if ball.xcor() <= -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1

    # ball and paddle collisions
    if (340 < ball.xcor() < 350) and ((paddle_b.ycor() - 40) < ball.ycor() < (paddle_b.ycor() + 40)):
        ball.setx(340)
        ball.dx *= -1
    if (-350 < ball.xcor() < -340) and ((paddle_a.ycor() - 40) < ball.ycor() < (paddle_a.ycor() + 40)):
        ball.setx(-340)
        ball.dx *= -1


