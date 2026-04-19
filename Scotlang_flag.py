import turtle

t = turtle.Turtle()

t.fillcolor("blue")
t.begin_fill()
t.forward(220)
t.left(90)
t.forward(100)
t.left(90)
t.forward(220)
t.left(90)
t.forward(100)
t.end_fill()

t.color("white")
t.width(10)
t.left(114)
t.forward(237)

# t.color("black")
t.penup()
t.left(155)
t.forward(216)

# t.color("red")
t.pendown()
t.left(157)
t.forward(237)

turtle.done()