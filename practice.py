import turtle
import random

screen = turtle.Screen()
screen.bgcolor("black")

# Player
player = turtle.Turtle()
player.shape("square")
player.color("green")
player.penup()
player.goto(0, -250)

# Enemy
enemy = turtle.Turtle()
enemy.shape("circle")
enemy.color("red")
enemy.penup()
enemy.goto(random.randint(-200, 200), 250)

# Movement
def left():
    player.setx(player.xcor() - 30)

def right():
    player.setx(player.xcor() + 30)

screen.listen()
screen.onkeypress(left, "Left")
screen.onkeypress(right, "Right")

while True:
    screen.update()

    enemy.sety(enemy.ycor() - 5)

    # Reset enemy
    if enemy.ycor() < -300:
        enemy.goto(random.randint(-200, 200), 250)

    # Collision
    if player.distance(enemy) < 20:
        player.goto(0, -250)