# Simple Pong in Python 3

import turtle

window = turtle.Screen()
window.title("PONG")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)  # Stops the window from updating

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)  #Speed of animation
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.color("white")
paddle_a.penup()
paddle_a.goto(-350, 0)


# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)  #Speed of animation
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.color("white")
paddle_b.penup()
paddle_b.goto(350, 0)


# Ball
ball = turtle.Turtle()
ball.speed(0)  #Speed of animation
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)

# Main game loop
while True:
    window.update()
